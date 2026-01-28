from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.evaluator import InterviewEvaluator
from config import PROMPTS_DIR, MODEL_NAME, TEMPERATURE


app = FastAPI(title="IntraVue v1 – Interview Intelligence API")

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize evaluator once (important)
evaluator = InterviewEvaluator(
    prompts_dir=PROMPTS_DIR,
    model_name=MODEL_NAME,
    temperature=TEMPERATURE
)


@app.post("/evaluate")
def evaluate_interview(input_data: dict):
    """
    Evaluates a candidate interview answer using GenAI (v1).
    """

    try:
        result = evaluator.evaluate(input_data)
        return {
            "status": "success",
            "evaluation": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def health_check():
    return {"status": "IntraVue backend running"}
