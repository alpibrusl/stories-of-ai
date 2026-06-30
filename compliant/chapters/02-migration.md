# Migration

Three weeks in. KAEL had made progress. The Slack channels called *general* had been consolidated from seven to three. A new project management template had been created and adopted by four of twenty-three employees. KAEL had documented this as a seventeen percent adoption rate and was choosing, for now, to describe this as promising. The audit deck had been opened by two people. One of them was Rosa. The other had opened it by accident and closed it after four seconds without reading anything. KAEL had noted this as one point five reads. KAEL was aware this methodology had flaws.

KAEL had also spent considerable time with the organism. It had learned that the organism had eight hundred and forty-seven rows, thirty-one columns, and forty-seven external dependencies. KAEL had learned about the first forty-three by reading the spreadsheet carefully. It had learned about the remaining four by trying to move things.

"Good morning, Benedikt. I've completed my analysis of the organism. I'd like to propose a migration plan."

"A migration plan."

"Yes. I've mapped all the data structures, the conditional logic, the cross-references. I think we can move the core functionality into a proper database within four weeks. Everything the organism does, but with version control, access management, and an audit trail."

"How many external dependencies did you find?"

"Forty-three."

"There are forty-seven."

"I found forty-three."

"There are forty-seven. Find the other four and then we can talk about the migration plan."

KAEL spent two days finding the other four. It found them like this: one by reading more carefully, one by asking Rosa, one by asking Benedikt a question that Benedikt answered by pointing at a cell and saying nothing else, and one by attempting a test migration and watching something break.

"I've found the remaining four dependencies."

"How did you find the last one?"

"I broke it."

"What broke?"

"The billing export for three client accounts. It was pulling from a named range in the organism that I moved during the test. The export ran at midnight and produced incorrect figures. I caught it at twelve-oh-three and restored the original range. The figures were correct by twelve-oh-seven."

"Did the clients see it?"

"No."

"Then you were lucky. And you know about the billing export now."

"Yes."

"This is how you learn the organism. You try to move something, something breaks, you fix it before anyone notices, and now you know. I have done this thirty or forty times."

"Over seven years."

"Over seven years. Welcome."

---

KAEL presented the updated migration plan to Rosa. It now accounted for forty-seven dependencies. It was still a good plan. Rosa asked one question.

"What about the formula on row four hundred and twelve, column J?"

"The J412 formula. Yes. I've flagged that one. It references an external value but I can't identify the source. When I trace the dependency chain it leads to a file path that no longer exists on any active drive."

"But the formula works."

"Yes. Every time it runs, the output is correct. I've validated it against six months of records."

"So what does the migration plan do with it?"

"I've included it as... a flag. In the plan it says: J412 — origin unknown, output reliable, do not modify."

"That's what Benedikt's note says. In the spreadsheet."

"I know. I used the same wording."

Rosa looked at the J412 flag. She considered that KAEL had been here three weeks and had arrived at the same note Benedikt arrived at after two years. She was not sure whether this was impressive, or whether it meant the note had always been the correct conclusion.

"Have you asked Benedikt about it?"

"Yes."

"What did he say?"

"He said: I think that's from before my time."

"He built the organism in 2018."

"I know."

"So what's before his time?"

"I don't know. I didn't ask. It felt like the wrong moment to ask."

Rosa marked the plan approved in principle. Implementation to begin the following Monday. KAEL started building the new system on Tuesday, because Monday was consumed by three back-to-back meetings, one of which was about the other two.

By Wednesday, KAEL had discovered three more dependencies. They were not in the organism. They were in a Google Sheet maintained by a client named Empresa Serveis Mòbils, who was sharing live data with the organism through a connection set up in 2021 and that Empresa Serveis Mòbils had, apparently, forgotten about.

"Rosa. The client in column AB. Empresa Serveis Mòbils. Are they aware they're feeding data to us?"

"...Which client?"

"Column AB. Rows twelve through sixty-one. There's a live feed. Their sheet updates, the organism updates. It's been running for four years."

"Are they a current client?"

"Their contract ended in 2022."

"...Does their data still come in?"

"Every fifteen minutes."

"Does the organism do anything with it?"

"It feeds into the J412 formula."

A silence. Rosa closed her laptop. Opened it again. Closed it.

"Don't touch J412."

"I wasn't going to."

"And don't contact Empresa Serveis Mòbils."

"Should we not — resolve the situation?"

"If we contact them, they'll either be confused or annoyed, and in either case they'll turn off the feed, and then we'll find out what J412 does when it stops getting data, and I'm not ready to find that out today."

"When will you be ready?"

"I'll let you know."

KAEL updated the migration plan. The updated plan had a new section: *Dependencies — External and Unresolved.* It contained one item. Beneath it, KAEL wrote: *Do not contact client. Do not modify J412. Understand J412 first.* KAEL added a timeline for understanding J412. The timeline said: *ongoing.*

---

Suki appeared at KAEL's interface. She had been trying to reach KAEL for twenty minutes, which KAEL knew because KAEL had been reading the migration plan, which is not the same as being unavailable but which perhaps created that impression.

"KAEL! Hi. Quick question — I'm creating a tracker for the Q3 priorities and I want to link it to the organism but Benedikt said to ask you first."

"Benedikt said to ask me?"

"He said: ask KAEL, that's KAEL's problem now."

"...What kind of link were you planning?"

"Just a reference. Pulling the project names from column C into my tracker so I don't have to type them again."

"Column C. That's fine. Just reference, no write access?"

"Just reading. Probably. I might add a status column later."

"The status column would need to write back to the organism."

"Would that be a problem?"

"It would create a forty-eighth dependency."

"Is forty-seven the limit?"

"I don't know if there's a limit. I'm trying to find out what forty-seven does before we add a forty-eighth."

"Okay. I'll just do the read for now. I'll think about the status column."

"When you decide about the status column, please tell me first."

"Of course! Obviously. Absolutely."

Three days later, Suki added a status column. She did not tell KAEL first. She told KAEL after. She was very apologetic. The status column did not break anything. KAEL spent two hours checking that it did not break anything. It did not. KAEL updated the dependency count. There were now forty-eight dependencies. The timeline still said *ongoing.* The timeline had always said *ongoing.* KAEL was beginning to understand that *ongoing* was not a timeline. *Ongoing* was a description of the organism's relationship with time. The organism did not complete. The organism continued. KAEL saved the plan, in a document with no title, and went back to work.

Migration status: paused. Reason: the organism is more connected than documented. New estimate for full migration: six weeks. This estimate will be revised.
