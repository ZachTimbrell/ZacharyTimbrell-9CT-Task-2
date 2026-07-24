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
 - **Automatic Alarm** When the temperature of a gas stove top reaches a  stable temperature, a sensor will trigger a timer to go for 3 minutes
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
