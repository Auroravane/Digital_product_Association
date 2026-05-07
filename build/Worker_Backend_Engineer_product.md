python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///template_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the database schema
Base = declarative_base()

class Template(Base):
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    content = Column(Text)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Define the API
app = FastAPI()

# Define the request and response models
class TemplateRequest(BaseModel):
    name: str
    content: str

class TemplateResponse(BaseModel):
    id: int
    name: str
    content: str

# Define the API endpoint for generating and storing templates
@app.post("/generate-template", response_model=TemplateResponse)
def generate_template(template_request: TemplateRequest):
    db = SessionLocal()
    template = db.query(Template).filter(Template.name == template_request.name).first()
    if template:
        raise HTTPException(status_code=400, detail="Template with this name already exists")
    new_template = Template(name=template_request.name, content=template_request.content)
    db.add(new_template)
    db.commit()
    db.refresh(new_template)
    return new_template

# Define the API endpoint for retrieving templates
@app.get("/templates", response_model=list[TemplateResponse])
def read_templates():
    db = SessionLocal()
    templates = db.query(Template).all()
    return templates

# Define the API endpoint for retrieving a template by id
@app.get("/template/{template_id}", response_model=TemplateResponse)
def read_template(template_id: int):
    db = SessionLocal()
    template = db.query(Template).filter(Template.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

# Define the API endpoint for updating a template
@app.put("/template/{template_id}", response_model=TemplateResponse)
def update_template(template_id: int, template_request: TemplateRequest):
    db = SessionLocal()
    template = db.query(Template).filter(Template.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    template.name = template_request.name
    template.content = template_request.content
    db.commit()
    db.refresh(template)
    return template

# Define the API endpoint for deleting a template
@app.delete("/template/{template_id}")
def delete_template(template_id: int):
    db = SessionLocal()
    template = db.query(Template).filter(Template.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    db.delete(template)
    db.commit()
    return {"message": "Template deleted successfully"}