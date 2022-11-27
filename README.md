## Expressing FISA's Definition of Electronic Surveillance with Logic - CPSC 415 - Project 2
### Anjali Gupta, Graham Stodolski, and Nick Weinberger

To run, type python main.py in the Terminal and enter your surveillance choices in the GUI.
 
(f)“Electronic surveillance” means—
(1)the acquisition by an electronic, mechanical, or other surveillance device of the contents of any wire or radio communication sent by or intended to be received by a particular, known United States person who is in the United States, if the contents are acquired by intentionally targeting that United States person, under circumstances in which a person has a reasonable expectation of privacy and a warrant would be required for law enforcement purposes;
∀D ∀P surveillance(D) ^ ∃C (radio(C) ∨ wire(C))  ^  acquire(D, C) ^ us_person(P) ^ target(P) ^ ∃ L (sent_loc_us(L, C, P) ∨ rec_loc_us(L, C, P)) ^ REP_LE(P)
∀D mech(D) ∨ electronic(D) → surveillance(D)
 
(2)the acquisition by an electronic, mechanical, or other surveillance device of the contents of any wire communication to or from a person in the United States, without the consent of any party thereto, if such acquisition occurs in the United States, but does not include the acquisition of those communications of computer trespassers that would be permissible under section 2511(2)(i) of title 18;
∀D ∀P surveillance(D) ^ us_person(P) ^ target(P) ^ ∃C wire(C) ^  ∃ L (sent_loc_us(L, C, P) ∨ rec_loc_us(L, C, P)) ^ ¬ consent(P) ^ acq_loc_us(L, C, P) ^ ¬is_perm(C) ^ acquire(D, C) 
 
(3)the intentional acquisition by an electronic, mechanical, or other surveillance device of the contents of any radio communication, under circumstances in which a person has a reasonable expectation of privacy and a warrant would be required for law enforcement purposes, and if both the sender and all intended recipients are located within the United States; or
∀D ∀P ∃C ∃e radio(C) ^ acquire(D, C) ^ intention(C) ^ surveillance(d) ^ REP_LE(P) ^ ∃ L sent_loc_us(L, C, P) ^ int_rec_loc_us(L, C, P)
 
(4) the installation or use of an electronic, mechanical, or other surveillance device in the United States for monitoring to acquire information, other than from a wire or radio communication, under circumstances in which a person has a reasonable expectation of privacy and a warrant would be required for law enforcement purposes.
∀D surveillance(D) ^ us_device(D) ^ REP_LE(P) ^  ∃C ¬(radio(C) ∨ wire(C)) ^ monitor(C)
