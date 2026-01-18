#!/usr/bin/env python3
"""
IELTS Audio Generation Script
Generates 50 MP3 audio files for Organ/Blood Donation topic
Using ElevenLabs API with diverse voices
"""

import os
from elevenlabs import ElevenLabs, VoiceSettings

# Initialize ElevenLabs client
client = ElevenLabs()

# Create output directory
os.makedirs("/home/ubuntu/English-IELTS-TRAINING-/tests/Organ_and_Blood_Donation_EXAM/audio", exist_ok=True)

# Define diverse voices for IELTS listening sections (using actual available voices)
VOICES = {
    "british_female": "EXAVITQu4vr4xnSDxMaL",  # Sarah - Mature, Reassuring
    "british_male": "JBFqnCBsd6RMkjVDRZzb",    # George - Warm Storyteller
    "american_male": "cjVigY5qzO86Huf0OWal",   # Eric - Smooth, Trustworthy
    "american_female": "cgSgspJ2msm6clMCkdW9", # Jessica - Playful, Bright
    "educator": "Xb7hH8MSUJpSbSDYk0k2",        # Alice - Clear Educator
    "professional": "XrExE9yKIg1WjnnlVkGX",    # Matilda - Professional
}

# Organ and Blood Donation Listening Scripts - 50 audio files
ORGAN_DONATION_SCRIPTS = [
    # Section 1 - Blood Donation Centre Dialogue (25 files)
    {"filename": "OBD_S1_01_intro.mp3", "voice": "british_female",
     "text": "Good morning, welcome to the Manchester Blood Donation Centre. How can I help you today?"},
    {"filename": "OBD_S1_02_response.mp3", "voice": "british_male",
     "text": "Hi, good morning. I'd like to register as a blood donor. I've been meaning to do this for quite a while."},
    {"filename": "OBD_S1_03_staff.mp3", "voice": "british_female",
     "text": "That's wonderful to hear. We're always in need of new donors. Let me take some details from you. Can I start with your full name?"},
    {"filename": "OBD_S1_04_name.mp3", "voice": "british_male",
     "text": "Yes, it's Michael Thompson."},
    {"filename": "OBD_S1_05_dob_question.mp3", "voice": "british_female",
     "text": "Thank you, Michael. And your date of birth?"},
    {"filename": "OBD_S1_06_dob_answer.mp3", "voice": "british_male",
     "text": "The 15th of March, 1992."},
    {"filename": "OBD_S1_07_address_question.mp3", "voice": "british_female",
     "text": "15th March 1992. And your current address?"},
    {"filename": "OBD_S1_08_address_answer.mp3", "voice": "british_male",
     "text": "I live at 47 Oakwood Road, Manchester."},
    {"filename": "OBD_S1_09_postcode.mp3", "voice": "british_female",
     "text": "47 Oakwood Road. And the postcode?"},
    {"filename": "OBD_S1_10_postcode_answer.mp3", "voice": "british_male",
     "text": "M14 6PL."},
    {"filename": "OBD_S1_11_occupation.mp3", "voice": "british_female",
     "text": "M-1-4, 6-P-L. Perfect. And what do you do for a living, Michael?"},
    {"filename": "OBD_S1_12_occupation_answer.mp3", "voice": "british_male",
     "text": "I'm a software engineer. I work for a tech company in the city centre."},
    {"filename": "OBD_S1_13_blood_type.mp3", "voice": "british_female",
     "text": "Lovely. Now, do you happen to know your blood type?"},
    {"filename": "OBD_S1_14_blood_type_answer.mp3", "voice": "british_male",
     "text": "Yes, I had it tested a few years ago. I'm O positive."},
    {"filename": "OBD_S1_15_process_explanation.mp3", "voice": "british_female",
     "text": "O positive – that's excellent. O positive is the most common blood type and is always in high demand. Now, you mentioned you've been meaning to donate for a while. How long have you been thinking about it?"},
    {"filename": "OBD_S1_16_how_long.mp3", "voice": "british_male",
     "text": "Oh, several months actually. I kept putting it off, but a colleague at work donated recently and it inspired me to finally come in."},
    {"filename": "OBD_S1_17_eligibility.mp3", "voice": "british_female",
     "text": "Well, I'm glad you're here now. Let me explain the process. First, we need to make sure you meet our eligibility criteria. You need to be at least 17 years old and weigh at least 50 kilograms."},
    {"filename": "OBD_S1_18_confirm_eligible.mp3", "voice": "british_male",
     "text": "I'm 31 and I weigh about 75 kilos, so that should be fine."},
    {"filename": "OBD_S1_19_donation_time.mp3", "voice": "british_female",
     "text": "Perfect. On the day of your donation, you'll have a brief health screening where we'll check your haemoglobin levels and ask some questions about your medical history. Then you'll be taken to the donation area. The actual blood donation itself is quite quick – it only takes about 5 to 10 minutes."},
    {"filename": "OBD_S1_20_surprised.mp3", "voice": "british_male",
     "text": "Oh, that's faster than I expected."},
    {"filename": "OBD_S1_21_aftercare.mp3", "voice": "british_female",
     "text": "Yes, many people are surprised. After you've donated, we ask that you rest for about 10 to 15 minutes and have some refreshments – tea, coffee, biscuits – to help your body recover. It's important not to rush off immediately."},
    {"filename": "OBD_S1_22_straightforward.mp3", "voice": "british_male",
     "text": "That sounds very straightforward."},
    {"filename": "OBD_S1_23_appointment.mp3", "voice": "british_female",
     "text": "It really is. Now, let me book you in for an appointment. We have availability next Saturday at 10:30 in the morning. Would that work for you?"},
    {"filename": "OBD_S1_24_confirm_appointment.mp3", "voice": "british_male",
     "text": "Yes, Saturday morning is perfect for me."},
    {"filename": "OBD_S1_25_closing.mp3", "voice": "british_female",
     "text": "Excellent. I've booked you in for next Saturday at 10:30 am. Please remember to drink plenty of water before you come and have a good breakfast."},
    
    # Section 2 - Organ Donation Awareness Presentation (10 files)
    {"filename": "OBD_S2_01_intro.mp3", "voice": "professional",
     "text": "Good afternoon, everyone, and thank you for attending today's session. My name is Sarah Collins, and I'm the Organ Donation Coordinator here at St. Mary's Hospital. The main purpose of my presentation today is to raise awareness about organ donation and to address some common questions and misconceptions."},
    {"filename": "OBD_S2_02_statistics.mp3", "voice": "professional",
     "text": "Let me start with some sobering statistics. Currently, around 7,000 people in the UK are on the transplant waiting list, hoping for a life-saving organ. Tragically, approximately three people die every day while waiting because there simply aren't enough organs available."},
    {"filename": "OBD_S2_03_law_change.mp3", "voice": "professional",
     "text": "Now, many of you may be aware that there was a significant change to England's organ donation law in 2020. An opt-out system was introduced, which means that all adults are now considered to have agreed to donate their organs when they die, unless they have recorded a decision not to donate or are in an excluded group."},
    {"filename": "OBD_S2_04_organs.mp3", "voice": "professional",
     "text": "In terms of which organs can be donated, the kidney is the most commonly transplanted organ. This is partly because we have two kidneys and can live healthily with just one, which makes living donation possible. Other organs that can be transplanted include the heart, liver, lungs, pancreas, and small intestine."},
    {"filename": "OBD_S2_05_family.mp3", "voice": "professional",
     "text": "I want to emphasise something very important: even with the new opt-out law, discussing your donation wishes with your family remains very important. Families are still consulted before donation proceeds, and knowing what their loved one wanted makes this conversation much easier during an already difficult time."},
    {"filename": "OBD_S2_06_key_facts.mp3", "voice": "professional",
     "text": "Let me share some key facts. A single organ donor can save up to eight lives through organ donation, and can help many more through tissue donation. However, organs must be transplanted within hours of recovery due to time constraints – they simply cannot survive outside the body for long."},
    {"filename": "OBD_S2_07_living_donation.mp3", "voice": "professional",
     "text": "For those interested in living donation, it's possible to donate a kidney or part of your liver while you're still alive. The liver is remarkable in that it can regenerate to its full size within a few months."},
    {"filename": "OBD_S2_08_nhs.mp3", "voice": "professional",
     "text": "The NHS Blood and Transplant service maintains the waiting list and coordinates all organ donation and transplantation in the UK. If you'd like to register your decision – whether to donate or not – you can do so on the NHS Organ Donor Register."},
    {"filename": "OBD_S2_09_closing.mp3", "voice": "professional",
     "text": "Finally, I cannot stress enough how important it is for families to know their relatives' wishes about donation. Having this conversation now, while everyone is healthy, can prevent uncertainty and distress later."},
    {"filename": "OBD_S2_10_questions.mp3", "voice": "professional",
     "text": "Thank you for your attention. I'll now take any questions you may have about organ donation or the registration process."},
    
    # Section 4 - Lecture on Blood Transfusion and Organ Preservation (15 files)
    {"filename": "OBD_S4_01_intro.mp3", "voice": "educator",
     "text": "Good afternoon, everyone. Today's lecture focuses on the science behind blood transfusion and organ preservation – two areas that are fundamental to modern transplant medicine."},
    {"filename": "OBD_S4_02_blood_tissue.mp3", "voice": "educator",
     "text": "Let's begin with blood. Blood is often described as a living tissue – and indeed it is. Unlike solid organs, blood can be transferred between individuals relatively easily, provided certain compatibility requirements are met. This makes blood transfusion one of the most common and life-saving medical procedures performed worldwide."},
    {"filename": "OBD_S4_03_landsteiner.mp3", "voice": "educator",
     "text": "The foundation of safe blood transfusion lies in understanding blood types. In 1901, Karl Landsteiner made the groundbreaking discovery that blood types are determined by antigens on the surface of red blood cells. He identified three blood types initially – A, B, and O – and his colleagues later identified the fourth type, AB."},
    {"filename": "OBD_S4_04_discovery.mp3", "voice": "educator",
     "text": "This discovery explained why some transfusions had been successful while others had caused fatal reactions. Landsteiner was awarded the Nobel Prize in 1930 for this groundbreaking work."},
    {"filename": "OBD_S4_05_rh_factor.mp3", "voice": "educator",
     "text": "The Rh factor, another crucial element of blood typing, was discovered later. It was named after experiments conducted on rhesus monkeys in the 1940s. People are classified as Rh positive or Rh negative depending on whether they have this antigen. Combined with the ABO system, this gives us the eight common blood types we recognise today."},
    {"filename": "OBD_S4_06_storage.mp3", "voice": "educator",
     "text": "Modern blood banking allows us to store blood for extended periods. Whole blood can be stored for up to 42 days under proper refrigeration at temperatures between 2 and 6 degrees Celsius."},
    {"filename": "OBD_S4_07_fractionation.mp3", "voice": "educator",
     "text": "The process of separating blood into its components – red cells, plasma, and platelets – is called fractionation. This allows us to use each component for different medical purposes and extends the utility of each donation."},
    {"filename": "OBD_S4_08_organ_preservation.mp3", "voice": "educator",
     "text": "Now, let's turn to organ preservation, which presents far greater challenges. Unlike blood, solid organs begin to deteriorate rapidly once removed from the body. The goal of organ preservation is to slow this deterioration long enough to transport the organ and perform the transplant."},
    {"filename": "OBD_S4_09_heart.mp3", "voice": "educator",
     "text": "Different organs have different preservation times. The heart is particularly time-sensitive – it can only be preserved for 4 to 6 hours outside the body. The main challenge is maintaining its continuous function, as the heart muscle is extremely sensitive to oxygen deprivation."},
    {"filename": "OBD_S4_10_liver.mp3", "voice": "educator",
     "text": "The liver can be preserved for 12 to 18 hours. The key challenge here is preventing cell damage that occurs when blood flow is interrupted and then restored."},
    {"filename": "OBD_S4_11_kidneys.mp3", "voice": "educator",
     "text": "Kidneys are more resilient and can be preserved for 24 to 48 hours, giving them the longest viable preservation time of the major organs. This relative durability is one reason kidney transplants are the most common."},
    {"filename": "OBD_S4_12_lungs.mp3", "voice": "educator",
     "text": "Lungs are extremely delicate and can only be preserved for 6 to 8 hours. Their complex structure makes them particularly vulnerable to damage."},
    {"filename": "OBD_S4_13_pancreas.mp3", "voice": "educator",
     "text": "Finally, the pancreas can be preserved for 12 to 24 hours, but it has complex metabolic requirements that make preservation challenging."},
    {"filename": "OBD_S4_14_new_techniques.mp3", "voice": "educator",
     "text": "Researchers continue to develop new preservation techniques, including machine perfusion, which keeps organs functioning outside the body by pumping them with oxygenated solutions. These advances are extending preservation times and improving transplant outcomes."},
    {"filename": "OBD_S4_15_closing.mp3", "voice": "educator",
     "text": "In conclusion, both blood transfusion and organ preservation represent remarkable achievements in medical science. Understanding the principles behind these procedures helps us appreciate the complexity of transplant medicine and the importance of donation. Thank you for your attention."},
]

def generate_audio(script_item, output_dir):
    """Generate audio for a single script item"""
    voice_id = VOICES.get(script_item["voice"], VOICES["british_female"])
    output_path = os.path.join(output_dir, script_item["filename"])
    
    try:
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text=script_item["text"],
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True
            )
        )
        
        # Save audio to file
        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        
        print(f"✓ Generated: {script_item['filename']}")
        return True
    except Exception as e:
        print(f"✗ Error generating {script_item['filename']}: {str(e)}")
        return False

def main():
    output_dir = "/home/ubuntu/English-IELTS-TRAINING-/tests/Organ_and_Blood_Donation_EXAM/audio"
    
    print("=" * 60)
    print("IELTS Audio Generation - Organ and Blood Donation")
    print("=" * 60)
    print(f"Total scripts to generate: {len(ORGAN_DONATION_SCRIPTS)}")
    print()
    
    success_count = 0
    for i, script in enumerate(ORGAN_DONATION_SCRIPTS, 1):
        print(f"[{i}/{len(ORGAN_DONATION_SCRIPTS)}] ", end="")
        if generate_audio(script, output_dir):
            success_count += 1
    
    print()
    print("=" * 60)
    print(f"Generation complete: {success_count}/{len(ORGAN_DONATION_SCRIPTS)} files created")
    print("=" * 60)

if __name__ == "__main__":
    main()
