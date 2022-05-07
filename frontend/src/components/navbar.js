import { BiWalletAlt } from 'react-icons/bi';
import { FaUserSecret } from 'react-icons/fa'
import { Wallet } from './wallet'
export const Navbar = ({ user, setUser, showWallet, setShowWallet, showPayment, setShowPayment, setLoading }) => {

    return (
        <div className="fixed w-full h-16 bg-purple-700 flex justify-between items-center px-4 md:px-24">
            <div className="text-white font-semibold text-xl">
                PyConKE
            </div>
            <div>
                <div className="relative hover:bg-purple-300 p-2 rounded-full hover:shadow-md">
                    {
                        !user &&
                        <BiWalletAlt size={28} className="cursor-pointer" color={"#FFFFFF"}  onClick={()=>{setShowWallet(prevState=>(!prevState))}}/>
                        ||
                        <FaUserSecret size={24} className="cursor-pointer"  onClick={()=>{setShowWallet(prevState=>(!prevState))}}/>
                    }
                    {
                        (showWallet || showPayment) &&
                        <Wallet user={user} setUser={setUser} showPayment={showPayment} setShowPayment={setShowPayment} setLoading={setLoading}/>
                    }
                </div>
            </div>
        </div>
    )
}
