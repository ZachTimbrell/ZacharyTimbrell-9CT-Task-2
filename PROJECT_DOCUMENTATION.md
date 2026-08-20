# Project Documentation
## Requirements Outline
### The need
The frequency of accidental fires in Australia has increased in the last couple of years. Fires can be caused from many reasons, such as naturally causes(bushfires fromn sunlight, lightning strikes, and volcanic activity) but are mainly caused by human error. Some instances include neglect ushc as unattended cooking, overload in powerstrips/excess electricty and poor management causes many fires annually

### The solution
We will design an alarm system that will detect when a stove top has been left on and unattended for more than 3 minutes using heat sensors. It will then make a highly intense noise to notify the user. There will also be a button which if pressed will set a 5 minute timer, lighting an LED that slowly gets brighter the more the timer decreases.

### Key Actions
- **Automatic Alarm:** After 3 minutes left unattended, an intense alarm will sound
- **Timer:** click a button to start a 5 minute timer to leave stove
- **Stack Button** everytime you click teh button, the timer will add 5 minutes to the downtime
- **LED Brightness** while the timer is on, an LED will slowing increase its brightness until the time is up.
- **Alarm** There will be another intense buzzer after the 5 minutes is complete
- **How to turn off** The alarm will not turn off once sounded unless the user clicks a button

### Functional Requirements
 - **Automatic Alarm** When the temperature of a gas stove top exceeding 100 degrees, a sensor will trigger a timer to go for 3 minutes
 - **Timer**: when clicked, the program must start a timer that lasts 5 minutes
 - **Stack Button** when clicked multiple times, program stacks the 5 mins
 - **LED brightness Timer** LED must light up when button clicked then increase in brightness over the 5 minutes
 - **Alarm**: After the 5 minute timer is completed, a buzzer will ring continuously
 - **End Button**: Once clicked, the ringing alarm will turn off

 ### Test Cases
 | Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|      Stove on for 3 minutes     |   heat sensor detects high temperature        |       high pitch alarm rings            |
|    button is pressed twice       |      button presses are detected     |        LED turn on(dim) and gets brighter as the timer decrease           |
|    Normal day       |       Heat sensors dont detect anything    |         nothing happens, no LED's turn on          |

### Non-Functional Requirements:
- The heat sensors should consistently detect heat input once per second
- buttons should always turn off timer and stack alarm time
- LED should always go from dim to bright depending the deuration the timer is on for.
- The code should be simple yet efficent so that we can understand it.

### Psudocode:

MAIN:

IMPORT time
	BEGIN 

		While true : 
			Read temp()
			IF temp() > 100 degrees:
				Run Automatic_Alarm
			ELSE 
				IF button() pressed = 0 then
			IF button pressed > 1
				Run 7 min alarm
				Run LED_Brightness()
			ELSE
				Run Stack
				Run LED_Brightness()
				ENDIF
			ENDIF
		ENDIF
		IF timer() = 0 THEN:
			OUTPUT Noise()
			IF Button_2() pressed THEN 
			END Noise()
			Sleep timer (1 second)
		ENDIF
	ENDWHILE


	BEGIN Stack
		WHEN button pressed
		Add 5 mins to timer()
	END Stack

	BEGIN LED_Brightness()
		IF timer() > timer()
		Add 0.05 brightness
		
	

### Flow Chart:
https://excalidraw.com/#json=GSN6XUadniQtGOj8Z4L-2,SQSbc6Oab721o4Cz8i2ZSA
### PMI
Kevin Zhu
- Plus: The circuitry functions properly, without any visible errors or misplaced wiring. In the end the program achieves its task(to dected heat at a harming rate and output an alarm) with the use of a heat sensors, buttons, an led and a buzzer
- Minus: The demo was a little bit too long, in the middle where nothing happend. 
- Implication: A way to improve for future tasks is to add efficient code but overall the program works flawlessly

Alfonso Delgado
- Plus: Nice clean code - sets up all the variables and needed pins in a clear and orderly way. Has clear comments, explaining how each line of code functions. Works as intended. Smart use of space - using two circut boards.
- Minus: wires can maybe be organised. Smart use of space - using two circut boards
- Implication: A way you can improve this is to make the buttons more distinct, such as maybe colour the end button red.

### Evaluation:

#### Evaluate your Final Test in Relation to Functional Criteria
Our final product demonstrated our functional criteria on point, we took into account each aspect of the functional requirements to help our circut be efficient yet simple. We included an automatic alarm that when the temperature reached higher than 100 degrees celcius for more than 3 minutes would set of a high pitch noise, we had a stack button function that when the user pressed button one, it would add 5 minutes to the automatic alarm, so that the user could be able to use the stovetop for however long they needed to, We also added an led which would display the timer decreasing by would getting brighter every 20% of the time, finally we added a second button that would turn off the alarm so that it was more simplistic and easier for the user to use. Overall we effectively completed the funactional points of out task.

#### Evaluate your Final Test in Relation to Non-Functional Criteria
Our final test met all of our non-functional requirements, which aided in the efficiency, accuracy, simplicity and response time of our project. For starters we made sure that the temperature wasnt constantly checked and instead only made it check once per second to improve longvevity and not waste power since we didnt believe that our project should be checking too often. For our second non-functional requirement we made sure that the stack and end buttons worked effectively and accurately when testing our design, we made the LED brighten automatically as the timer decreased no matter what the stack is by using a percentage of the total timer, and finally we made the code simple to understand by adding comments to each part of the code which majorly helped us in the coding stages. In general we cohesively utalised our non-functional requirements outline to support us in the making of our circuitry and code.
#### Evaluate your Final Performance in Relation to the Identified Need
The final performance of our task in relation to the identified need was relatively well imposed. We planned to making a working alarm system for stove tops, where an alarm will go off automatically if a gas stove has been left on for a long period of time, or you can individually stack(5 mins per button click) an reminding timer which will eventually sound an alarm to remind you that you stove is still on and the circut can also sense whether the stove has been turned off and therefore will deactivate the timer automatically. Inclusively our design and code effectively completed this plan to almost perfection, we believe there there are only little improvements needed for our project to be perfect.
#### Evaluate your Project in Relation to Project Management
I believe I managed my time well throughout this assessment task, despite needing to complete major parts of the development and integration unit into the testing and debugging stage, this is because i was away on  Ski trip for all of week 4. For the first 3 weeks, I stuck to the plan given to us and completed the project documentation thoroughly. And for the last 2 weeks, my buddy and I have conversed with each other to make sure the final product is as it was intended to be.
#### Evaluate your Project in Relation to Peer Feedback.
Our peer feeback overall was very positive and helpful, the two people that viewed out task gave good responses that ould help us improve for future assessment tasks. The first person, Kevin, stated that our project over was clean and effective, and gave us some room for improvement in the area of making the demo video a little shorter which would be a quick fix, for the future he suggests to make the code more effecient. Our second peer, Alfonso, highlighted our code was clean and understandable due to the comments we added along the way, he suggested that the wires could be a little more organised and he stated that in the future we would make the buttons more distinct by adding a different colour of look to each one, so it doesnt become confusing. Overall the feeback from our peers was good yet helpful.
#### Justify Future Improvements you could make to your Final Product
I belive that our final product could have been improved in some aspects, as it is just a prototype we did not put it near a flame and changed the sensored temp to room temperature, but if we were to make this for real I would make sure the whole project was fire resistant and more sturdy. I think we could have improved the cleanliness of our wires because at some areas it was hard to understand what wires were going where, aswell as this I think the idea to make each of the button more unique to each other was a good idea that could easily make it mrore understandable, aswell as a read me for the circuitry. These improvements were very minor but would boost the usability of our design overall.