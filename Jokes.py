import json, requests, os , sys
######################################################
#		    	 KEY 			     #
#	                                             #
#	#### = Start or End of Function 	     #
#	                                             #
#	# = notes and simple comments  	             #
# 						     #
#	### = Explanation of function processes      #
#                                                    #
#	######### = End of Functions in Class	     #
#						     #
#	##### = section identifier 		     #
#                                                    #
#                                                 -MA#
######################################################
class randomJokeApi:
	def getJoke():
	####Start of getJoke()
		#first we will call the API through the link
		apiResponse = requests.get("https://v2.jokeapi.dev/joke/Any")
		#we will then load it into a json string
		responseLoad = json.loads(apiResponse.text)
		
		def pullnPrint():
		####Start of pullnPrint
		###Function will be used to form the joke
			if(responseLoad["type"] != "single"):
				print("Hello Murphy!!!\nThe Joke of the Day is:\n")
				print("\t",responseLoad["setup"],"\n")
				print("\t",responseLoad["delivery"],"\n")
			else:	
				print("Hello Murphy!!!\nThe Joke of the Day is:\n")
				print("\t",responseLoad["joke"])
		####End of pullnPrint()
		
				
		def checknStart():
		####Start of checknStart()	
		###List of checks to return values for different issues 
			#error check
			if( responseLoad["flags"]["nsfw"] or responseLoad["flags"]["racist"] or responseLoad["flags"]["sexist"] != False):	
				print("Hello! This Joke has been removed by Developers due to offensiveness, restarting the program!")
				#this next line restarts the code a runs the program again  if theres something racist, sexist, or if theres an error. Thanks jlliagre
				os.execl(sys.executable, sys.executable, *sys.argv)
			else:	
				#if there is no errors or offensive comments, pull the joke. 
				pullnPrint()
		####End of checknStart()

		#now we are back in getJoke(), we will kickstart checknStart()
		checknStart()			
	####End of getJoke()
			#########END OF FUNCTIONS IN CLASS#########
	

	#####Run Sequence#####
	###run our main function
	getJoke()
		
