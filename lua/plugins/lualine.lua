return {
	'nvim-lualine/lualine.nvim',
	config = function()
	require('lualine').setup({	
		option = {
			theme = 'dracula'
		},
		sections = {
			lualine_c = {{ 'filename', path=2}}
		},
	})
	end
}


