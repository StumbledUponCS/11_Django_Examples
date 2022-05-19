To work on your Django project :




		To Create a virtual environment :

				Navigate to where you want the project to be located 

						python -m venv myproject






You must activate the virtual environment every time you open the command prompt to work on your project.




	1) Navigate to where your project is located (from root to the directory containing your 

		myproject directory)


	

	2) *** Activate your Environment : ****

		
			source myproject/bin/activate



	3) Once the environment is activated, you will see this result in the command prompt:


			Unix/MacOS:

			(myproject) ... $


		
	3) To Check your version of Python :


			python --version


	4) To Check your version of PIP :
			

			pip --version
    

	4) To Check your version of Django :
	

			django-admin --version



	5) To Start a New Project :


			django-admin startproject <projectName>


	6) To Run the new project and see it on a web browser :
				
				Naviage into the root folder


					python manage.py runserver


	7) To See the Result :

			Open a new browser window and type 

					127.0.0.1:8000 

						in the address bar.


	8) To Create an App :
			
			python manage.py startapp <appName>

			
				then update views.py, create urls.py, and folder templates 
	

	9) You can add to views direction for what to do during the app

			add to urls --> call views

	11) you can add a templates folder and add html docs inside

			to connect it to the view add to view
				add that to url patterns so it can call that method in views





	10) To make migrations : (happens after changes, for changes to take effect, such as creating 
					models, adding to models or updating)


			python manage.py makemigrations <ModelName>

					** done when adding to models

			python manage.py migrate

					** done when adding to templates and models

	11) To add to a model :
				

				Open a Python shell :

						python manage.py shell

				
						from <RootFolderName>.models import <ModelName>

	

						<ModelName>.objects.all()




						x = <ModelName>(attribute1='', attribute2='')
						x.save()





						<ModelName>.objects.all().values()





						a = <ModelName>(attribute1='', attribute2='')
						b = <ModelName>(attribute1='', attribute2='')
						c = <ModelName>(attribute1='', attribute2='')
						d = <ModelName>(attribute1='', attribute2='')
						e = <ModelName>(attribute1='', attribute2='')

						member_list = [a, b, c, d, e]

						for y in member_list:
							y.save()



						<ModelName>.objects.all().values()




				To exit the shell :
						


						quit()





				

					
				a = <ModelName>(firstname ='Harry', lastname='Potter')
				b = <ModelName>(firstname ='Hermonie', lastname ='Granger')
				c = <ModelName>(firstname ='Ron', lastname ='Weasley')
				d = <ModelName>(firstname ='Ginny', lastname ='Weasley')
				e = <ModelName>(firstname ='Draco', lastname ='Malfoy')
