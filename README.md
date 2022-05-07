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
