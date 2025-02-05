class Profile:
    def __init__(self, cvl_path="resources/coverletter.txt", mailbody_path="resources/mailbody.txt", cv_path="resources/cv.txt"):
        self.cvl_path = cvl_path
        self.mailbody_path = mailbody_path
        self.cv_path = cv_path
        self.cover_letter = open(cvl_path, "r")
        self.mail_body = open(mailbody_path, "r")
        self.cv = open(cv_path, "r")
'''      
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
'''  