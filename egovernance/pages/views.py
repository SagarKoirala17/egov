from django.shortcuts import render, redirect
from .models import Citizen
import io
from django.http import FileResponse
import reportlab.pdfgen
from django.contrib import messages


# Create your views here.
def index(request):

    if request.method == "POST":


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob = request.POST["dob"]
        phone = request.POST["Phone"]
        age = request.POST["Age"]
        father_name = request.POST["fathername"]
        mother_name = request.POST["mothername"]
        husband_name = request.POST["husbandname"]
        grandfather_name = request.POST["grand_father_name"]
        father_citizen_number = request.POST["father_citizenship_number"]
        mother_citizen_number = request.POST["mothercitizenshipnumber"]
        husband_citizen_number = request.POST["husbandcitizenshipnumber"]
        birth_certificate_photo = request.POST["birthcerificatephoto"]
        father_citizenship_photo = request.POST["fathercitizenship"]
        mother_citizenship_photo = request.POST["mothercitizenship"]
        husband_citizenship_photo = request.POST["husbandcitizenship"]
        p_zone = request.POST["Zone"]
        p_district = request.POST["District"]
        p_village = request.POST["Village/Municipality"]
        p_ward = request.POST["Ward no"]
        p_tole = request.POST["Tole"]
        p_house_no = request.POST["House no."]
        t_zone = request.POST["zone1"]
        t_district = request.POST["district1"]
        t_village = request.POST["village1"]
        t_ward = request.POST["ward1"]
        t_tole = request.POST["tole1"]
        t_house_no = request.POST["house1"]

        if request.user.is_authenticated:







            citizen = Citizen(first_name=first_name, last_name=last_name, email=email, dob=dob,
                          phone=phone, age=age, father_name=father_name, mother_name=mother_name,
                          husband_name=husband_name,
                          grandfather_name=grandfather_name, father_citizen_number=father_citizen_number,
                          mother_citizen_number=mother_citizen_number,
                          husband_citizen_number=husband_citizen_number,
                          father_citizenship_photo=father_citizenship_photo,
                          mother_citizenship_photo=mother_citizenship_photo,
                          husband_citizenship_photo=husband_citizenship_photo,
                          t_zone=t_zone, t_district=t_district, t_village=t_village, t_ward=t_ward, t_tole=t_tole,
                          t_house_no=t_house_no, p_zone=p_zone, p_district=p_district, p_village=p_village,
                          p_ward=p_ward,
                          p_tole=p_tole,p_house_no=p_house_no)

            citizen.save()



            messages.success(request, "Your form has been submitted to the admin")
            return redirect('index')
        else:
            message.success(request,"You must login first to submit the form")
            return redirect('login')






    else:

        return render(request, 'pages/index.html')
