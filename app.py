##############################################################
#### Written By: SATYAKI DE                               ####
#### Written On: 11-Apr-2024                              ####
#### Modified On 14-Apr-2024                              ####
####                                                      ####
#### Objective: This new solution will to evaluate and    ####
#### enhance Generative AI applications by using UpTrain, ####
#### Open AI & Python. It offers grading for over 20       ####
#### preconfigured checks across language, code, and      ####
#### embedding scenarios.                                 ####
####                                                      ####
##############################################################

from clsConfigClient import clsConfigClient as cf
import clsL as log

from datetime import datetime, timedelta
from openai import OpenAI

import random
import time
from uptrain import EvalLLM, Evals, CritiqueTone
import json
import re
import clsTemplate as ct

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and all origins

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

########################################################
################    Global Area   ######################
########################################################

fileDBPath = cf.conf['DB_PATH']

var1 = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print('*' *60)
DInd = cf.conf['DEBUG_IND']
OPENAI_API_KEY = cf.conf['OPEN_AI_KEY']

eval_llm = EvalLLM(openai_api_key=OPENAI_API_KEY)

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    api_key=cf.conf['OPEN_AI_KEY'],
    max_retries=0,
    timeout=20.0,
)

templateVal_1 = ct.templateVal_1
########################################################
################  End Of Global Area   #################
########################################################

def askFeluda(context, question):
    try:
        # Combine the context and the question into a single prompt.
        prompt_text = f"{context}\n\n Question: {question}\n Answer:"

        # Retrieve conversation history from the session or database
        conversation_history = []

        # Add the new message to the conversation history
        conversation_history.append(prompt_text)

        # Call OpenAI API with the updated conversation
        response = client.with_options(max_retries=0).chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_text,
                }
            ],
            model=cf.conf['MODEL_NAME'],
            max_tokens=150,  # You can adjust this based on how long you expect the response to be
            temperature=0.3,  # Adjust for creativity. Lower values make responses more focused and deterministic
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the content from the first choice's message
        chat_response = response.choices[0].message.content

        # Print the generated response text
        return chat_response.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def evalContextRelevance(question, context, resFeluda, personaResponse):
    try:
        data = [{
            'question': question,
            'context': context,
            'response': resFeluda
        }]

        results = eval_llm.evaluate(
            data=data,
            checks=[Evals.CONTEXT_RELEVANCE, Evals.FACTUAL_ACCURACY, Evals.RESPONSE_COMPLETENESS, Evals.RESPONSE_RELEVANCE, CritiqueTone(llm_persona=personaResponse), Evals.CRITIQUE_LANGUAGE, Evals.VALID_RESPONSE, Evals.RESPONSE_CONCISENESS]
        )

        return results
    except Exception as e:
        x = str(e)

        return x

# Function to handle malformed JSON-like strings
def preprocessParseData(value):
    try:
        # Convert the value to a string if it's not already one
        context = str(value)
        question = templateVal_1

        value_str = askFeluda(context, question)

        return value_str  # Return original if no JSON structure is detected
    except:
        value_str = ''

        return value_str

# Function to extract and print all the keys and their values
def extractPrintedData(data):
    for entry in data:
        print("Parsed Data:")
        for key, value in entry.items():


            if key == 'score_context_relevance':
                s_1_key_val = value
            elif key == 'explanation_context_relevance':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_1_val = cleaned_value
            elif key == 'score_factual_accuracy':
                s_2_key_val = value
            elif key == 'explanation_factual_accuracy':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_2_val = cleaned_value
            elif key == 'score_response_completeness':
                s_3_key_val = value
            elif key == 'explanation_response_completeness':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_3_val = cleaned_value
            elif key == 'score_response_relevance':
                s_4_key_val = value
            elif key == 'explanation_response_relevance':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_4_val = cleaned_value
            elif key == 'score_critique_tone':
                s_5_key_val = value
            elif key == 'explanation_critique_tone':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_5_val = cleaned_value
            elif key == 'score_fluency':
                s_6_key_val = value
            elif key == 'explanation_fluency':
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_6_val = cleaned_value
            elif key == 'score_valid_response':
                s_7_key_val = value
            elif key == 'score_response_conciseness':
                s_8_key_val = value
            elif key == 'explanation_response_conciseness':
                print('Raw Value: ', value)
                cleaned_value = preprocessParseData(value)
                print(f"{key}: {cleaned_value}\n")
                s_8_val = cleaned_value

    print('$'*200)

    results = {
        "Factual_Accuracy_Score": s_2_key_val,
        "Factual_Accuracy_Explanation": s_2_val,
        "Context_Relevance_Score": s_1_key_val,
        "Context_Relevance_Explanation": s_1_val,
        "Response_Completeness_Score": s_3_key_val,
        "Response_Completeness_Explanation": s_3_val,
        "Response_Relevance_Score": s_4_key_val,
        "Response_Relevance_Explanation": s_4_val,
        "Response_Fluency_Score": s_6_key_val,
        "Response_Fluency_Explanation": s_6_val,
        "Response_Tonality_Score": s_5_key_val,
        "Response_Tonality_Explanation": s_5_val,
        "Guideline_Adherence_Score": s_8_key_val,
        "Guideline_Adherence_Explanation": s_8_val,
        "Response_Match_Score": s_7_key_val
        # Add other evaluations similarly
    }

    return results

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json

    if not data:
        return {jsonify({'error': 'No data provided'}), 400}

    # Extracting input data for processing (just an example of logging received data)
    question = data.get('question', '')
    context = data.get('context', '')
    llmResponse = ''
    personaResponse = data.get('personaResponse', '')
    guideline = data.get('guideline', '')
    groundTruth = data.get('groundTruth', '')
    evaluationMethod = data.get('evaluationMethod', '')

    print('question:')
    print(question)

    llmResponse = askFeluda(context, question)
    print('='*200)
    print('Response from Feluda::')
    print(llmResponse)
    print('='*200)

    # Getting Context LLM
    cLLM = evalContextRelevance(question, context, llmResponse, personaResponse)

    print('&'*200)
    print('cLLM:')
    print(cLLM)
    print(type(cLLM))
    print('&'*200)

    results = extractPrintedData(cLLM)

    print('JSON::')
    print(results)

    resJson = jsonify(results)

    return resJson

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
