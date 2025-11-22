import streamlit as st
import pickle


st.title('Titanic Survival Prediction App!')
st.image('titanic.jpg', caption = 'Predict Survival on the Titanic')

#Load the Pretrained Model
with open('titanicpickle1.pkl', 'rb') as pickleFile:
    model = pickle.load(pickleFile)

#Function to Make Prediction
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    try:
        prediction = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]) # 0 or 1
        return 'Survived' if prediction[0] == 1 else 'Did not Survive'
    except Exception as e:
        return f'Error: {str(e)}'



#Sidebar for Instructions
st.sidebar.header('HOW TO USE!')
st.sidebar.markdown("""
1.Enter the Passenger Details in the Form.
2.⁠Click 'Predict' to see the survival result.
3.⁠Adjust values to test different scenarios.                   
""")
st.sidebar.info('Example: A 30 years old male, 3rd class passenger, $20 fare, traveling alone from port Southempton.')

#Main Input Form
def main():
    st.subheader('Enter Passenger Details: ')
    col1, col2 = st.columns(2)
    #organize Inputs in Columns
    with col1:
        Pclass = st.selectbox('Passenger Class:', options = [1,2,3], format_func = lambda X: f'class{X}')
        Sex = st.radio('Sex: ', options = ['male', 'female'])
        Age = st.slider('Age: ', min_value=0,max_value=100, value=30)
    with col2:
        SibSp = st.slider('Siblings/Spouses Aboard: ', min_value=0, max_value=10, value=0)
        Parch = st.slider('Parents/Children Aboard: ', min_value=0, max_value=10, value=0)
        Fare = st.slider('Fare($): ', min_value=0.0, max_value=500.0, value=50.0, step=0.1)
        Embarked = st.radio('Port of Embarkation: ', options=['C', 'Q', 'S'], format_func = lambda X :f'port{X}')
    #Convert Categorical Inputs to Numerical Values
    Sex = 1 if Sex == 'female' else 0
    Embarked = {'C': 0, 'Q':1, 'S':2}[Embarked]
    #Button for prediction
    if st.button('Predict'):
        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        st.markdown(f'{result}')

        if result == 'Survived':
            st.balloons()
main()