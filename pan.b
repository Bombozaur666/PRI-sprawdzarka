	switch (t->back) {
	default: Uerror("bad return move");
	case  0: goto R999; /* nothing to undo */

		 /* CLAIM L4 */
;
		;
		;
		;
		
	case 5: // STATE 13
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM L3 */
;
		;
		;
		;
		
	case 8: // STATE 13
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM L2 */
;
		;
		;
		;
		
	case 11: // STATE 13
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* CLAIM L1 */
;
		;
		
	case 13: // STATE 13
		;
		p_restor(II);
		;
		;
		goto R999;

		 /* PROC P */

	case 14: // STATE 1
		;
		((P0 *)_this)->i = trpt->bup.oval;
		;
		goto R999;

	case 15: // STATE 2
		;
	/* 0 */	((P0 *)_this)->i = trpt->bup.oval;
		;
		;
		goto R999;

	case 16: // STATE 5
		;
		((P0 *)_this)->tmp = trpt->bup.oval;
		;
		goto R999;

	case 17: // STATE 6
		;
		((P0 *)_this)->tmp = trpt->bup.oval;
		;
		goto R999;

	case 18: // STATE 7
		;
		now.a = trpt->bup.oval;
		;
		goto R999;

	case 19: // STATE 8
		;
		((P0 *)_this)->i = trpt->bup.oval;
		;
		goto R999;

	case 20: // STATE 12
		;
		p_restor(II);
		;
		;
		goto R999;
	}

