from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Album
# from django.http import Http404
# import csv
# from django.core.mail import send_mail
from django.core.mail import EmailMessage


def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums}
	# template = loader.get_template('myapp/index.html')
	# return HttpResponse(template.render(context, request))
	return render(request, 'myapp/index.html', context)


def detail(request, album_id):
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'myapp/detail.html', {'album': album})


def upload_csv(request):
	return render(request, 'myapp/csvupload.html')


def upload_csv_process(request):
	if request.method == 'POST':
		csv_email = []
		if len(request.FILES) != 0 and str(request.FILES['fileUpload']).endswith(".csv"):
			csv_email.extend(handle_uploaded_file(request.FILES['fileUpload'], str(request.FILES['fileUpload'])))

		login_data = request.POST.dict()
		email_to = list(filter(None, str(login_data.get('email')).replace(" ", "").split(","))) + csv_email
		ccemail = list(filter(None, str(login_data.get('ccemail')).replace(" ", "").split(",")))
		bccemail = list(filter(None, str(login_data.get('bccemail')).replace(" ", "").split(",")))
		subject = str(login_data.get('subject'))
		body = str(login_data.get('body'))

		if len(email_to) == 0 or not subject or not body:
			print("Please enter valid details to send email")
			return HttpResponse("Please enter valid details to send email")
		else:
			send_mail(subject, body, email_to, ccemail, bccemail)
			return HttpResponse("Sending mail...")

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


def send_mail(subject, body, to_mail, cc_mail, bcc_mail):
	# html_content = "<strong>Comment tu vas?</strong>"
	email = EmailMessage(subject, body, "test@test.com", to_mail, bcc_mail, None, None, None, cc_mail, None)
	email.content_subtype = "html"
	res = email.send()
	print("Email Res: " + str(res))
