import streamlit as st
import functions as fun

todos = fun.read_todos()
def add_todo():
    todo = st.session_state["new_todo"] + '\n'

    todos.append(todo)

    fun.write_todos(todos)

st.title("My Todo APP")
st.subheader("This is running on my local machine")
st.write("This is write a statement on webapp")




for num, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=num)
    if checkbox:
        todos.pop(num)
        fun.write_todos(todos)
        del st.session_state[num]
        st.rerun()
st.text_input(placeholder="Add new todo:",
              label="",
              on_change=add_todo,
              key="new_todo")
