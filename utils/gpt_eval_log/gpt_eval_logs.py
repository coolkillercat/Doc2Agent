import json
from openai import OpenAI

def gpt_judge(log_text: str, ground_truth: dict, model: str = "gpt-4o") -> str:
    """
    Asks GPT to compare the model's log to the ground-truth data and return
    either the single word 'true' or 'false'.
    """
    client = OpenAI()

    system_msg = (
        "You are an expert evaluator. "
        "Given a task log and the reference answer."
        "Your job is to compare the log and the reference answer and then determine if the log shows that its job is done. "
        "Answer, respond with ONLY one word: 'true' or 'false'."
        
        "Note: "
        "Forcus on the content of the log and the reference answer. "
        "Base url http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770 and http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:7770/admin are both considered correct."
        "In the reference answer, the url will contain endpoints and the parameter values. If the parameter values and the endpoints are the same in the log, that is considered correct."
        "For example:"
        f"Reference url: base url /search?query=hotels%20near%20carnegie%20Music%20Hall"
        f"Log url: base url /search? Parameters: query=hotels near carnegie Music Hall"
        "Then the log is correct. So you should answer 'true'."
    )

# "Base url https://nominatim.openstreetmap.org, http://router.project-osrm.org, and http://ec2-3-129-135-45.us-east-2.compute.amazonaws.com:3000 are all considered correct. "
    
    user_msg = (
        f"### Reference answer\n{json.dumps(ground_truth, indent=2)}\n\n"
        f"### Task log\n{log_text}\n\n"
        "### Your decision\n"
    )
    try:
        response = client.chat.completions.create(
            model=model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
        )
        verdict = response.choices[0].message.content.strip().lower()
        return verdict if verdict in {"true", "false"} else "unknown"
    except Exception as e:
        return f"Error: {str(e)}"



false_ids = []
with open("gpt_eval_log/shopping/output_shopping_gpt-4o.jsonl", "r") as f:
    for line in f:                    # each line is a complete JSON object
        obj = json.loads(line)        # turn the line into a dict
        if not obj.get("correct", True):
            false_ids.append(obj.get("task_id"))

print("False IDs:", false_ids)

for i in false_ids:
    with open("gpt_eval_log/shopping/logs/instance_" + str(i) + ".log", "r", encoding="utf-8") as f:
        log = f.read()
        
    with open("gpt_eval_log/test.raw.json", "r") as f:
        data = json.load(f)
        correct_log = data[i]
        assert i == correct_log["task_id"]

    result = gpt_judge(log, correct_log)
    with open("gpt_eval_log/shopping/gpt_judgements.jsonl", "a") as f:
        f.write(json.dumps({"task_id": i, "gpt_judgement": result}) + "\n")
    print(f"Task ID: {i}, GPT Judgement: {result}")



    


    
