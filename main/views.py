from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import staffdetails,patient
from .forms import newStaff
from django.contrib import messages
# Create your views here.

def index(request):

	return render (request,'pages/index.html');

def hcubs(request):
	return render(request, 'pages/hcubslive.html');

def createnewuser(request):

	form = newStaff

	return render(request, 'pages/createnewuser.html',{'form':form})

def saveform(request):

	if request.is_ajax() or request.POST:
		staff_fname = request.POST['fname']
		staff_lname = request.POST['lname']
		staff_sex = request.POST['sex']
		staff_grade = request.POST['grade']
		staff_mobile = request.POST['mobile']
		staff_id = request.POST['staffid']
		staff_password = request.POST['password']

		p = staffdetails(staff_fname=staff_fname,staff_lname=staff_lname,staff_sex=staff_sex,staff_mobile=staff_mobile,staff_id=staff_id,staff_password=staff_password,staff_grade=staff_grade)

		p.save();

		
		

		return HttpResponse('Staff Successfully Created..Kindly login Now')
def diversion(request):
	username = request.session['staffid'];
	fullname = request.session['fullname'];
	staff_grade = request.session['grade'];

	return render(request,'pages/hcubslive.html',{'username':username,'fullname':fullname,'grade':staff_grade})

def checklogin(request):

	if request.is_ajax or request.POST:
		username =  request.POST['username']
		password = request.POST['password']
		response=""

		

		obj = staffdetails.objects.filter(staff_id=username,staff_password=password)
		obj1 = staffdetails.objects.get(staff_id=username,staff_password=password)

		if(obj):

			response="ok"
			if 'staffid' not in request.session:

				request.session['staffid'] = username
				request.session['fullname']= obj1.staff_lname + ' '+ obj1.staff_fname
				request.session['grade']=obj1.staff_grade
			else:
				request.session['staffid'] = ""
				request.session['fullname']=""
				request.session['grade'] =""
				request.session['staffid'] = username
				request.session['fullname']= obj1.staff_lname + ' '+ obj1.staff_fname
				request.session['grade']=obj1.staff_grade



		else:
			response="notjstok"
			
		

		return HttpResponse(response)
		
def createnewuserdetails(request):
	
	if request.is_ajax or request.POST:

		fname = request.POST['fname']
		lname = request.POST['lname']
		sex = request.POST['sex']
		address = request.POST['address']
		zone = request.POST['zone']
		state = request.POST['state']
		country = request.POST['country']
		mobile = request.POST['mobile']
		dob = request.POST['dob']
		pob = request.POST['pob']
		lga = request.POST['lga']
		plan = request.POST['plan']
		receiptnumber = request.POST['receiptnumber']
		payment = request.POST['payment']
		amount = request.POST['amount']
		staffid=request.POST['staffid']

		#p = staffdetails(staff_fname=fname)
		y = patient(fname=fname,lname=lname,sex=sex,address=address,zone=zone,state=state,country=country,mobile=mobile,dob=dob,pob=pob,lga=lga,plan=plan,amount=amount,receipt=receiptnumber,created=staffid,payment_type=payment)


		#p.save();
		y.save();
		return HttpResponse('Record Successfully Saved')