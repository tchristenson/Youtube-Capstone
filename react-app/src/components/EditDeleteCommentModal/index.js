import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";


function EditDeleteCommentModal() {
    const dispatch = useDispatch()

    const {closeModal} = useModal()

    const handleEdit = async (e) => {
        e.preventDefault()


    }

    const handleDelete = async (e) => {
        e.preventDefault()

    }


    return (
        <>
            <div>
                <form onSubmit={handleEdit}>
                    <button type="submit">Edit</button>
                </form>
            </div>

            <div>
                <form onSubmit={handleDelete}>
                <button onClick={closeModal}>Delete</button>
                </form>
            </div>
        </>
    )
}

export default EditDeleteCommentModal
