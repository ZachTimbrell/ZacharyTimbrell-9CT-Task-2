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
- Implication: A way to improve for future tasks is to add efficient code but overall

Alfonso Delgado
- Plus: Nice clean code - sets up all the variables and needed pins in a clear and orderly way. Has clear comments, explaining how each line of code functions. Works as intended. Smart use of space - using two circut boards.
- Minus: wires can maybe be organised. Smart use of space - using two circut boards
- Implication: A way you can improve this is to make the buttons more distinct, such as maybe colour the end button red.

### Evaluation:

Evaluate your Final Test in Relation to Functional Criteria

Evaluate your Final Test in Relation to Non-Functional Criteria

Evaluate your Final Performance in Relation to the Identified Need

Evaluate your Project in Relation to Project Management
I believe I managed my time well throughout this assessment task, despite needing to complete major parts of the development and integration unit into the testing and debugging stage, this is because i was away on  Ski trip for all of week 4. For the first 3 weeks, I stuck to the plan given to us and completed the project documentation thoroughly. And for the last 2 weeks, my buddy and I have conversed with each other to make sure the final product is as it was intended to be.
Evaluate your Project in Relation to Peer Feedback.

Justify Future Improvements you could make to your Final Product
