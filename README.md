# Mega-4th-Grade-BratBot
4th grade Python Intro to A.I. project

Earlier this year our fourth graders started thinking about, then building and testing, some very crude A.I. models.
The MegaBratBot project is a collaborative effort to give one particular model a good workout.

In this model, each 'bot' represents an identity, or perspective, that communicates with the outside world using a set of stock phrases the bot can draw upon when in conversational mode. 

In our first iteration, a phrase would be randomly selected from its library every time the bot has a chance to speak.

Initially we thought of some amusing communications paradigms that could be approximated by our model. 
In particular, we imagined some so-called "experts" who just resort to preset talking points without any real intelligence or discrimination involved.
- a "desktop support" agent that continually asks if you've updated your O/S, instructs you to reboot your computer, etc.
- a "conflict resolution" specialist that relies heavily on some well-worn phraseology*
- a political pundit
etc.

And the results were...frequently amusing. But usually the kids were able to quickly detect "fakeness" in our "expert" bots.

As we talked things over, we theorized that because children have relatively limited vocabulary, and are often given to slogans and catch phrases,
we thought that kids' playground "roasts" might lend themselves well to our crude model of human communication. 
For instance, witness the age-old technique of repeating exactly what someone else says;
or stock phrases like "I know you are, but what am I?" and "I'm the rubber, you're the glue," or "Sticks and stones may break my bones" etc.

So we modeled out a dozen bots based on actual students, and the Dev/Lab coders had the bright idea to pit the bots against each other in a Battle Royale of sorts.
It turns out that at least some of the time, the results actually simulated a plausible interaction between the two agents. 
Despite the high noise-to-signal ratio, seeing those moments when the models "clicked" is incredibly satisfying, and can lead to
some pretty interesting conversations about free will and the nature of language.

From a technical perspective, our next task is to talk about how to make the model more realistic: e.g. more dynamic and context-sensitive.
It seems that the only real "intelligence" in our current model lies in the code authors' canny selection of content--i.e. the intelligence still lies on the human side!


*Boomers may recall the famous early A.I./N.L.P. thought experiment called "Eliza" that simulated a Rogerian psychotherapist: https://en.wikipedia.org/wiki/ELIZA
