# Intro to Web3 Development with Python (PyconKE 2022)

> > Project to create generative art that users can mint NFTs on the blockchain. [Here is the link to the slides](https://github.com/GrishonNganga/PyconKe2022-.git)

## Structure

- Frontend App (/frontend folder) - ReactJS
- Backend App (app.py) - Flask
- Blockchain Stuff (blockchain.py) - Ganache, either install Ganache or deploy to a public testnet like Ropsten or Rinkeby
- Art Generation (art_generator.py) - All the logic to mix and match art's layers and creates final mintable image
- IPFS - (ipfs.py) - (Pinata) All artworks minted on the blockchain are store on IPFS.
- Inputs - NFTs are created by combining random artworks for the indivdual layers. The layers are in (layers/ folder) and are named by the layer they belong to followed by (\_[index]). eg. For 'background' layer we have an image called (bg_0.png).
- Outputs - All generated artworks are stores in (output/ folder) and in JSON formart in (generated_nfts.json) as a list of all the layers used to create the artwork.
- Rarity - For the individual layers, the is higher likelihood to get certain images than others, that is called digital rarity. We've implemented as: The first image in every layer collection has been set as the most rare. (That can hover be changed in _art_generator.py_)

That is just a basic breakdown of all the indivual components of the project. I'll be preparing an in depth step by step tutorial of doing all this so watch out for that on my [Twitter](https://twitter.com/Grishonnganga)
![Screenshot from 2022-05-07 10-07-55](https://user-images.githubusercontent.com/52824774/167243287-7d407977-a322-4986-9a3f-58ad59b7c1f4.png)
![Screenshot from 2022-05-07 10-10-22](https://user-images.githubusercontent.com/52824774/167243284-8cba959b-c58e-494e-8471-daac4d0cd3c7.png)
![Screenshot from 2022-05-07 10-11-22](https://user-images.githubusercontent.com/52824774/167243281-d6ea6e10-a049-43ef-be68-58e4a6d79a15.png)
