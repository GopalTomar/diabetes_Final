import streamlit as st

def welcome():

    st.write(
        """
        <style>
            .box:hover{
                background-color: lightblue;
            }
            .dropdown {
                position: relative;
                display: inline-block;
            }
            .dropdown-content {
                display: none;
                position: absolute;
                background-color: white;
                min-width: 220px;
                color: black;
                text-decoration: none;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
            }
            .dropdown:hover .dropdown-content {
                display: block;
            }
            .dropdown-content a {
                padding: 12px 16px;
                display: block;
                text-decoration: none;
                color: black; /* added to make the text black */
            }
            .dropdown-content a:hover {
                background-color: lightblue;
            }
            .next {
                display: grid;
                grid-template-columns: repeat(2, 100px); 
                gap: 10px;
            }
            .child {
                # background-color: lightblue;
            }
            .black-text {
                color: black;
            }
        </style>
             








<div style="width: 100%; height: 300px; background-color: lightgrey; margin-top: 20px; border: 2px solid black; border-radius: 5px; -webkit-box-shadow: 12px 10px 20px 0px rgba(51,102,4,1);-moz-box-shadow: 12px 10px20px 0px rgba(51,102,4,1);box-shadow: 12px 10px 20px 0px rgba(51,102,4,1); background: rgb(223,247,247);background: linear-gradient(90deg, rgba(223,247,247,1) 1%, rgba(217,220,244,09612219887955182) 100%, rgba(0,236,255,1) 100%);">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: row;">
        <div>
            <h1 class="black-text"> Diabetes </h1>
        </div>
        <div>
        </div>
    </div>
    <div style="padding:20px">
        <h4 class="black-text">"Diabetes, a chronic condition, results from inadequate insulin production or ineffective use of insulin by the body. Symptoms include frequent urination, increased thirst, and unexplained weight loss. Diagnosis relies on blood tests measuring blood sugar levels. Treatment involves lifestyle modifications, medication, and insulin therapy, highlighting the importance of regular monitoring and management." 🚀 </h4>
        <button style="margin-top: 10px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;"><a href="https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFozaOzAZaq4C9gvq8UXYkUtkDTWYEoStZ3LVNxTSsKxhhDigNsiW6ShoC0wQQAvD_BwE#tab=tab_1" style="text-decoration:none;color:white;">To know more </a></button>
    </div>
</div>
<br>
    """,
        unsafe_allow_html=True,
    )


def main():
    st.title("Welcome to my Streamlit App")
    welcome()


if __name__ == "__main__":
    main()


