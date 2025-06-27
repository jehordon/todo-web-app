import streamlit as st
import functions as fns  # Assuming you have a functions.py with read_todos and write_todos

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Initialize the todos list by reading from the file
# Ensure this runs only once when the app first loads
if 'todos' not in st.session_state:
    st.session_state.todos = fns.get_todos()


# Function to handle checkbox click
def complete_todo():
    """
    Removes a todo item from the session_state.todos list
    based on the key of the checkbox that was just interacted with.
    """
    # Streamlit passes the key of the widget that triggered the callback
    # into session_state. We can then use this to identify the item.

    # We need to find which checkbox caused the callback.
    # The 'st.session_state' will reflect the current state of the widget
    # that triggered the callback.

    # Iterate through the keys in session_state to find the one that changed
    # and is now True (checked)

    # A more robust way to find the checked item:
    # We need to know which 'todo' was checked.
    # The checkbox's key stores a hint (the original index and todo text)
    # When the on_change fires, the value of that specific key in session_state
    # will be updated.

    # Find the index of the item to remove.
    # We'll use the current list of todos and iterate to find the match.
    # This is more robust than relying on `args=(idx,)` if the list
    # could shift between the last render and the callback execution.

    # Let's find the specific key that was just changed to True
    # (or rather, the checkbox that was just clicked)

    # The actual mechanism:
    # When a checkbox is clicked, st.session_state[its_key] is updated.
    # We want to remove the item *corresponding* to that key.

    # Let's rework the `on_change` to directly pass the todo string itself
    # and handle the index search internally. This is often safer.

    # This function is called WHEN a checkbox is clicked.
    # The `st.session_state` *already* reflects the new state of that checkbox.
    # We need to find WHICH checkbox's value just became True.

    # A better approach is to pass the specific todo text or its unique identifier.
    # However, since you are iterating and using `idx`, we need a way to relate
    # the callback back to the original `idx` reliably.

    # Let's reconsider the args. The `idx` passed via `args=(idx,)` is the `idx`
    # *at the time the checkbox was created*. If items have been removed prior
    # to this click in the same session, that `idx` might no longer be correct.

    # The safest way is to rebuild the list of todos *excluding* the one that
    # was just marked as complete.

    # This revised complete_todo takes no arguments and finds the item to remove
    # by looking at the session_state values.

    new_todos = []
    removed_a_todo = False
    for idx, todo in enumerate(st.session_state.todos):
        # Construct the same key used for the checkbox
        checkbox_key = f"checkbox_{idx}_{todo}"

        # Check if this checkbox's state in session_state is True (meaning it was just ticked)
        # and if it corresponds to the current todo.
        # This is where the trick lies: when the callback fires,
        # the session state for the specific checkbox that was clicked is updated.
        if st.session_state.get(checkbox_key) == True:
            # This item was ticked. DO NOT add it to new_todos.
            removed_a_todo = True
            # Also, remove its state from session_state to prevent ghosting if a new todo
            # is added later and happens to get the same key.
            del st.session_state[checkbox_key]
        else:
            # This item was not ticked, so keep it.
            new_todos.append(todo)

    if removed_a_todo:
        st.session_state.todos = new_todos
        fns.write_todos(st.session_state.todos)
        # No st.rerun() needed here! Streamlit will automatically rerun after the callback finishes.


# Display current todos with checkboxes
for idx, todo in enumerate(st.session_state.todos):
    # Use a unique key for each checkbox, combining index and todo text for robustness
    checkbox_key = f"checkbox_{idx}_{todo}"

    # Create the checkbox. The `on_change` callback is triggered when its value changes.
    # We don't need to set `value` explicitly here, as Streamlit manages it internally.
    # The `complete_todo` function will inspect `st.session_state` to find which one changed.
    st.checkbox(todo, key=checkbox_key, on_change=complete_todo)


# Function to add a new todo
def add_todo():
    new_todo = st.session_state.new_todo.strip()
    if new_todo:
        st.session_state.todos.append(new_todo)
        fns.write_todos(st.session_state.todos)
        st.session_state.new_todo = ""  # Clear the input box


st.text_input("Add a new todo:", on_change=add_todo, key="new_todo")