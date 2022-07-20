import React from 'react'

function Introduction() {
    return (
        <div>
            <p>
                SMS-Spam-Detection website utilizes the power of BERT NLP model.<br />
                The model is loaded to HuggingFace and can be found here:<br />
                <a href="https://huggingface.co/matanbn/smsPhishing">https://huggingface.co/matanbn/smsPhishing</a><br />
                Our research respository and training process:<br />
                <a href="https://github.com/matannagar/SMS_Spam_Detection_Web">https://github.com/matannagar/SMS_Spam_Detection_Web</a><br />
                This website was created by Matan-Ben Nagar to demonstrate the power of NLP using BERT.
            </p>
        </div>
    )
}

export default Introduction
