import React, {useEffect, useState} from 'react'

import {loadTodo} from '../lookup'

export function TodoComponent(props) {
    const textAreaRef = React.createRef()
    const [newTodo, setNewTodo] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newVal = textAreaRef.current.value
        let tempNewTodo = [...newTodo]
        tempNewTodo.unshift({
            content: newVal,
            assign: 0,
            id: 12314
        })
        setNewTodo(tempNewTodo)
        console.log(newVal)
        textAreaRef.current.value = ''
    }
    return <div className={props.className}>
            <div className='col-12 mb-3'>
                <form onSubmit={handleSubmit}>
                    <textarea ref={textAreaRef} required={true} className='form-control' name='todo'>

                    </textarea>
                    <button type='submit' className='btn btn-primary my-3'>Todo</button>
                </form>
            </div>
            <TodoList newTodo={newTodo} />
        </div>
}

export function TodoList(props) {
    const [todoInit, setTodoInit] = useState([])
    const [todo, setTodo] = useState([])
    useEffect(() => {
        const final = [...props.newTodo].concat(todoInit)
        if (final.length !== todo.length) {
            setTodo(final)
        }
    }, [props.newTodo, todo, todoInit])

    useEffect(() => {
        const myCallback = (status,response) => {
        console.log(status,response)
        if (status === 200){
            setTodoInit(response)
        } else {
            alert("Err")
        }
        }
    loadTodo(myCallback)
    }, [todoInit])
    return todo.map((item, index) => {
        return <Todo todo={item} className='my-5 py-5 bg-white text-dark' key={`${index}-{todo.id}`}/>
    })

    }

export function ActionBtn(props) {
    const {todo, action} = props
    const [assign, setAssign] = useState(todo.assign ? todo.assign : 0)
    const [userAssign, setUserAssign] = useState(todo.userAssign === true ? true : false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'assign') {
            if (userAssign === true) {
                setAssign(assign - 1)
                setUserAssign(false)
            } else {
            setAssign(assign + 1)
            setUserAssign(true)
            }
        }
    }
    const display = action.type === 'assign' ? `${assign} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
    }

export function Todo(props) {
    const {todo} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{todo.id}-{todo.content}</p>
        <div className='btn btn-group'>
        <ActionBtn todo={todo} action={{type:"assign", display:"Assign"}}/>
        <ActionBtn todo={todo} action={{type:"unassign", display:"Unassign"}}/>
        <ActionBtn todo={todo} action={{type:"retodo", display:"Retodo"}}/>


        </div>
    </div>
    }