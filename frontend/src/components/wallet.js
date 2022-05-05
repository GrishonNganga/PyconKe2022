import { useState } from 'react'
import bg from '../assets/bg.jpg'
import eth from '../assets/eth.png'
import crypto from '../assets/crypto.svg'
import loader from '../assets/round_loader.gif'
import { auth } from '../api/endpoints'

export const Wallet = ({ user, setUser }) => {

    return (
        <div className="absolute md:w-[360px] h-[400px] shadow-xl rounded-xl bg-white z-50 -left-72 top-12">
            {
                user &&
                <UserWallet user={user} />
                ||
                <CreateAccount setUser={setUser}/>
            }
        </div>
    )
}

const UserWallet = ({ user }) => {

    function copy() {
        navigator.clipboard.writeText(user)
    }

    return (
        <div className="w-full flex flex-col justify-center">
            <div className="w-full h-20 bg-gray-100 flex justify-between items-center p-8 gap-x-6">
                <div>
                    pY
                </div>
                <div className="flex gap-x-2">
                    <div className="flex gap-x-1.5 border-2 rounded-full items-center px-3 py-2 ">
                        <div className="w-4 h-4 bg-green-900 rounded-full">

                        </div>
                        <div>
                            Ethereum Local
                        </div>
                    </div>
                </div>
                <div>
                    <img src={bg} className="w-9 h-9 rounded-full object-cover" />
                </div>
            </div>
            <div className="w-full flex flex-col justify-center items-center border-b">
                <div className="flex flex-col justify-center px-2 mt-1 h-16 font-semibold text-gray-500 hover:bg-gray-100 rounded-md cursor-pointer" onClick={() => { copy() }}>
                    <div className="flex items-center">
                        <div className="text-xl tracking-wider">
                            Account
                        </div>
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                <path strokeLinecap="round" strokeLinejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                            </svg>
                        </div>
                    </div>
                    <div className="text-gray-300 text-xs">
                        {user.substring(0,5)}...{user.substring(user.length-4, user.length)}
                    </div>
                </div>
            </div>
            <div className="w-full flex justify-center my-2">
                <div className="border rounded-full p-1.5">
                    <img src={eth} className="w-8 h-8" />
                </div>
            </div>
            <div className="w-full flex flex-col items-center">
                <div className="text-3xl">
                    0 ETH
                </div>
                <div className="text-base text-gray-400">
                    KES 0.00
                </div>
            </div>
            <div className="w-full flex flex-col items-center my-2">
                <div className="p-1 bg-purple-700 rounded-full">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-white" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M16.707 10.293a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0l-6-6a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l4.293-4.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                </div>
                <div className="text-xs text-purple-700 font-semibold">
                    Buy
                </div>
            </div>
        </div>
    )
}

const CreateAccount = ({ setUser }) => {
    const [creatingAccount, setCreatingAccount] = useState("")
    const [createLoading, setCreateLoading] = useState(false)
    const [createError, setCreateError] = useState(false)
    const [importLoading, setImportLoading] = useState(false)
    const [importError, setImportError] = useState(false)
    const [user, setCreatedUser] = useState(null)

    const createAccount = () => {
        setCreatingAccount("create")
        setCreateLoading(true)
        auth().then(response => {
            setCreateLoading(false)
            console.log(response)
            if (response && response.status === 200) {
                setCreatedUser(response.data.key)
            } else {
                setCreateError("Something wrong happened")
            }
        })
    }

    const finishCreatingAccount = () => {
        setCreatingAccount(false)
        setUser(user)
    }
    return (
        <div className="h-full">
            {
                creatingAccount === "" &&
                <div className="w-full flex flex-col justify-center items-center">
                    <div className="text-xl my-5 font-semibold">
                        Add Account
                    </div>
                    <div className="w-2/3 my-2.5">
                        <img src={crypto} className="w-full" />
                    </div>
                    <div className="w-3/4 mt-6">
                        <div className="w-full">
                            <button className="w-full bg-purple-700 py-2.5 rounded-md hover:bg-purple-800 text-white font-semibold" onClick={createAccount}>
                                <span>Create Account</span>
                            </button>
                        </div>
                        <div className="w-full mt-6">
                            <button className="w-full bg-gray-200 py-2.5 rounded-md hover:bg-gray-300 text-gray-500 hover:text-gray-600 font-semibold" onClick={finishCreatingAccount}>
                                <span>Import Account</span>
                            </button>
                        </div>
                    </div>
                </div>
                ||
                (creatingAccount === "import") &&
                <div className="w-full flex flex-col justify-center items-center">
                    <div className="text-xl my-5 font-semibold">
                        Import Account
                    </div>
                    <div>

                    </div>
                </div>
                ||
                (creatingAccount === "create") &&
                <div className="h-full flex flex-col items-center">
                    <div className="text-xl my-5 font-semibold">
                        Create Account
                    </div>
                    {
                        createLoading &&
                        <div>
                            <img src={loader} />
                        </div>
                        ||
                        (!createError &&
                            <div className=" w-full p-2 flex flex-col shrink-0">
                                <div className="border-2 rounded-md p-2 truncate">
                                    {user.public}
                                </div>
                                <div className="text-xl font-semibold mt-6">
                                    Private Key
                                </div>
                                <div className="text-xs text-red-400 mt-2">
                                    Always keep your private key safe, you lose this, you lose everything
                                </div>
                                <div className="border-2 rounded-md p-3 line-clamp-3 mt-2">
                                    {user.private}
                                </div>
                                <div className="w-full mt-8">
                                    <div className="w-full">
                                        <button className="w-full bg-purple-700 py-2.5 rounded-md hover:bg-purple-800 text-white font-semibold" onClick={ finishCreatingAccount }>
                                            <span>Close</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            ||
                            <div className="text-red-500 bg-green-500">
                                {createError}
                            </div>
                        )
                    }
                </div>
            }
        </div>
    )
}