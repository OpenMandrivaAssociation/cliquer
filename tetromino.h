
#define TETROMINOS 19

struct polynomino tetromino[TETROMINOS] = {
	{ "straight", 1,4,
	  "#   "
	  "#   "
	  "#   "
	  "#   " },
	{ "straight 90deg", 4,1,
	  "####"
	  "    "
	  "    "
	  "    " },

	{ "l", 2,3,
	  "#   "
	  "#   "
	  "##  "
	  "    " },
	{ "l 90deg", 3,2,
	  "  # "
	  "### "
	  "    "
	  "    " },
	{ "l 180deg", 2,3,
	  "##  "
	  " #  "
	  " #  "
	  "    " },
	{ "l 270deg", 3,2,
	  "### "
	  "#   "
	  "    "
	  "    " },
	{ "l mirror", 2,3,
	  " #  "
	  " #  "
	  "##  "
	  "    " },
	{ "l mirror 90deg", 3,2,
	  "### "
	  "  # "
	  "    "
	  "    " },
	{ "l mirror 180deg", 2,3,
	  "##  "
	  "#   "
	  "#   "
	  "    " },
	{ "l mirror 270deg", 3,2,
	  "#   "
	  "### "
	  "    "
	  "    " },
	
	{ "t", 3,2,
	  "### "
	  " #  "
	  "    "
	  "    " },
	{ "t 90 deg", 2,3,
	  "#   "
	  "##  "
	  "#   "
	  "    " },
	{ "t 180 deg", 3,2,
	  " #  "
	  "### "
	  "    "
	  "    " },
	{ "t 270 deg", 2,3,
	  " #  "
	  "##  "
	  " #  "
	  "    " },

	{ "square", 2,2,
	  "##  "
	  "##  "
	  "    "
	  "    " },

	{ "skew", 3,2,
	  "##  "
	  " ## "
	  "    "
	  "    " },
	{ "skew 90deg", 2,3,
	  " #  "
	  "##  "
	  "#   "
	  "    " },
	{ "skew mirror", 3,2,
	  " ## "
	  "##  "
	  "    "
	  "    " },
	{ "skew mirror 90deg", 2,3,
	  "#   "
	  "##  "
	  " #  "
	  "    " }
};
