vim.g.mapleader = " "
vim.g.maplocalleader = ","
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
vim.keymap.set("n", "<leader>n", ":Neotree filesystem reveal left<CR>")
vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)
