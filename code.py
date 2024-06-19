def q_runner(self, query):
    try:
        # Execute the query and fetch the results into a DataFrame
        df = pd.read_sql_query(query, self.session.bind)
        
        # Commit the changes
        self.session.commit()
        
        return df
    
    except Exception as e:
        # Rollback the changes in case of an error
        self.session.rollback()
        return f"An error occurred: {str(e)}"
    
    finally:
        # Close the session
        self.session.close()
