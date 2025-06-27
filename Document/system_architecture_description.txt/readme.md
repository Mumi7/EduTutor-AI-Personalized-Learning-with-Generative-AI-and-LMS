system_architecture_description.txt
EduTutor AI - System Architecture Description

The system architecture of EduTutor AI is modular and scalable. It includes the following key components:

1. *Frontend (Streamlit UI)*  
   - Provides a simple user interface for students and teachers.  
   - Allows users to input queries and receive AI-generated content.

2. *Backend Services*  
   - Manages API endpoints and core application logic.  
   - Connects to AI services, the database, and external integrations.

3. *AI Integration (IBM Watsonx)*  
   - Powers the generative AI functionalities to deliver personalized learning content.

4. *Google Classroom Sync*  
   - Syncs assignments, lessons, and grades with users' Google Classroom accounts.

5. *Vector Database (Pinecone)*  
   - Stores and retrieves learning material using vector embeddings for fast similarity search.

6. *System Database*  
   - Handles user data, environment variables, and configurations.

This architecture supports a smooth and intelligent learning experience, personalized for each learner.
