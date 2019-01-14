from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .mail_actor import send_mail


def index(request):
	return HttpResponse("To send mail please enter: http://localhost:8000/myapp/upload_csv")


def upload_csv(request):
	return render(request, 'myapp/csvupload.html')


def upload_csv_process(request):
	if request.method == 'POST':
		csv_email = []
		if len(request.FILES) != 0 and str(request.FILES['fileUpload']).endswith(".csv"):
			csv_email.extend(handle_uploaded_file(request.FILES['fileUpload'], str(request.FILES['fileUpload'])))

		form_data = request.POST.dict()
		email_to = list(filter(None, str(form_data.get('email')).replace(" ", "").split(","))) + csv_email
		ccemail = list(filter(None, str(form_data.get('ccemail')).replace(" ", "").split(",")))
		bccemail = list(filter(None, str(form_data.get('bccemail')).replace(" ", "").split(",")))
		subject = str(form_data.get('subject'))
		body = str(form_data.get('body'))
		sendType = str(form_data.get('sendType'))
		print(sendType)

		if len(email_to) == 0 or not subject or not body:
			print("Please enter valid details to send email")
			return HttpResponse("Please enter valid details to send email")
		else:
			if sendType == 'all':
				send_mail(subject, body, email_to, ccemail, bccemail)
				return HttpResponse("Sending mail to all together")
			elif sendType == 'one':
				for mail in email_to:
					send_mail(subject, body, [mail], ccemail, bccemail)
				return HttpResponse("Sending mail one by one")
			else:
				return HttpResponse("Send type not found. Please try again.")
	return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
	file_data = file.read().decode("utf-8")
	lines = file_data.split("\n")
	str_list = list(filter(None, lines))
	str_list.pop(0)
	email_ids = []
	for line1 in str_list:
		email_ids.append(line1.split(',')[0])
	return email_ids


