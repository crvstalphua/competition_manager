from functions import input_teams, input_matches, display_rankings, display_team, edit_match, edit_team, clear, switch_frames
import logging
import tkinter as tk

logging.basicConfig(filename='comp_manager.log', level=logging.INFO, format='%(asctime)s %(message)s', filemode='w')

def main():

    root = tk.Tk()
    root.title('Competition Manager')
    root.geometry('800x500')
    root.resizable(False, False)
    root.configure(background='azure3')

    
    # team input page
    team_page = tk.Frame(root, background='azure3')
    
    t_label = tk.Text(team_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    t_label.pack()
    t_label.insert(tk.END, 'Input Teams: <Team Name> <Registration Date> <Group Number>')

    t_input = tk.Text(team_page, height=20, width=70)
    t_input.pack(pady=10)

    t_submit_button = tk.Button(team_page, text="Submit Teams", background='black', command=lambda: input_teams(None, t_input, t_log))
    t_submit_button.pack(pady=10)
    t_input.bind('<Return>', lambda event: (input_teams(event, t_input, t_log) if not event.state & 0x1 else None))

    t_log = tk.Text(team_page, font=('Ariel', '10'), height=4, width=70, bg='azure3', fg='black')
    t_log.pack()
    t_log.delete('1.0', 'end')

    t_return_button = tk.Button(team_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    t_return_button.pack(side=tk.BOTTOM, pady=10)
   

    # match input page
    match_page = tk.Frame(root, background='azure3')

    m_label = tk.Text(match_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    m_label.pack()
    m_label.insert(tk.END, 'Input Matches: <Team_1> <Team_2> <Team_1_Goals> <Team_2_Goals>')

    m_input = tk.Text(match_page, height=20, width=70)
    m_input.pack()

    m_submit_button = tk.Button(match_page, text="Submit Matches", background='black', command=lambda: input_matches(None, m_input, m_log))
    m_submit_button.pack(pady=10)
    m_input.bind('<Return>', lambda event: (input_matches(event, m_input, m_log) if not event.state & 0x1 else None))

    m_log = tk.Text(match_page, font=('Ariel', '10'), height=4, width=70, bg='azure3', fg='black')
    m_log.pack()
    m_log.delete('1.0', 'end')

    m_return_button = tk.Button(match_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    m_return_button.pack(side=tk.BOTTOM, pady=10)
    

    # ranking display page
    ranking_page = tk.Frame(root, background='azure3')

    r_label = tk.Text(ranking_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    r_label.pack()
    r_label.insert(tk.END, 'Display Rankings')

    r_label = tk.Text(ranking_page, font=('Ariel', '14'), height=20, width=70, bg='gray25', fg='white')
    r_label.pack()

    r_display_button = tk.Button(ranking_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    r_display_button.pack(side=tk.BOTTOM, pady=10)


    # team details page
    team_details_page = tk.Frame(root, background='azure3')

    td_label = tk.Text(team_details_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    td_label.pack()
    td_label.insert(tk.END, 'Retrieve Team Details: <Team Name>')

    td_input = tk.Text(team_details_page, height=10, width=70)
    td_input.pack(pady=10)

    td_submit_button = tk.Button(team_details_page, text="Submit Team Name", background='black', command=lambda: display_team(None, td_input, td_log))
    td_submit_button.pack(pady=10)
    td_input.bind('<Return>', lambda event: display_team(event, td_input, td_log))

    td_log = tk.Text(team_details_page, font=('Ariel', '12'), height=10, width=70, bg='azure3', fg='black')
    td_log.pack()
    td_log.delete('1.0', 'end')

    td_return_button = tk.Button(team_details_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    td_return_button.pack(side=tk.BOTTOM, pady=10)


    # team edit page
    team_edit_page = tk.Frame(root, background='azure3')

    te_label = tk.Text(team_edit_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    te_label.pack()
    te_label.insert(tk.END, 'Edit Team (Do not edit Name): <Team Name> <Registration Date> <Group Number>')

    te_input = tk.Text(team_edit_page, height=10, width=70)
    te_input.pack(pady=10)

    te_submit_button = tk.Button(team_edit_page, text="Submit Team Edits", background='black', command=lambda: edit_team(None, te_input, te_log))
    te_submit_button.pack(pady=10)
    te_input.bind('<Return>', lambda event: edit_team(event, te_input, te_log))

    te_log = tk.Text(team_edit_page, font=('Ariel', '12'), height=10, width=70, bg='azure3', fg='black')
    te_log.pack()
    te_log.delete('1.0', 'end')
    
    te_return_button = tk.Button(team_edit_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    te_return_button.pack(side=tk.BOTTOM, pady=10)


    # match edit page
    match_edit_page = tk.Frame(root, background='azure3')
    
    me_label = tk.Text(match_edit_page, font=('Ariel', '18'), height=1, width=70, bg='gray', fg='white')
    me_label.pack()
    me_label.insert(tk.END, 'Edit Match (team order does not matter): <Team_1> <Team_2> <Team_1_Goals> <Team_2_Goals>')

    me_input = tk.Text(match_edit_page, height=10, width=70)
    me_input.pack(pady=10)

    me_submit_button = tk.Button(match_edit_page, text="Submit Match Edits", background='black', command=lambda: edit_match(None, me_input, me_log))
    me_submit_button.pack(pady=10)
    me_input.bind('<Return>', lambda event: edit_match(event, me_input, me_log))

    me_log = tk.Text(match_edit_page, font=('Ariel', '12'), height=10, width=70, bg='azure3', fg='black')
    me_log.pack()
    me_log.delete('1.0', 'end')
    
    me_return_button = tk.Button(match_edit_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    me_return_button.pack(side=tk.BOTTOM, pady=10)


    # clear page
    clear_page = tk.Frame(root, background='azure3')

    c_label = tk.Label(clear_page, text='Data Cleared', background='azure3', font=('Ariel', '18', 'bold'))
    c_label.pack()

    c_return_button = tk.Button(clear_page, text="Return to Menu", background='black', command=lambda: menu_page.tkraise())
    c_return_button.pack(side=tk.BOTTOM, pady=10)

    

    # menu page
    menu_page = tk.Frame(root, background='azure3')
    menu_page.pack()

    for frame in (menu_page, team_page, match_page, ranking_page, team_details_page, team_edit_page, match_edit_page, clear_page):
        frame.grid(row=0, column=0, sticky='news')

    tk.Label(menu_page, text='Home Menu', font=('Ariel', '16', 'bold'), bg='azure3').pack(padx=10, pady=10)

    team_input_button = tk.Button(menu_page, text='Add Teams', height=2, width=40, command=lambda: team_page.tkraise())
    team_input_button.pack(pady=10)
    match_input_button = tk.Button(menu_page, text='Add Matches', height=2, width=40, command=lambda: match_page.tkraise())
    match_input_button.pack(pady=10)
    ranking_button = tk.Button(menu_page, text='Display Team Rankings', height=2, width=40, command=lambda: [display_rankings(r_label), ranking_page.tkraise()])
    ranking_button.pack(pady=10)
    team_details_button = tk.Button(menu_page, text='Retrieve Team Details', height=2, width=40, command=lambda: team_details_page.tkraise())
    team_details_button.pack(pady=10)
    team_edit_button = tk.Button(menu_page, text='Edit Team Details', height=2, width=40, command=lambda: team_edit_page.tkraise())
    team_edit_button.pack(pady=10)
    match_edit_button = tk.Button(menu_page, text='Edit Match Details', height=2, width=40, command=lambda: match_edit_page.tkraise())
    match_edit_button.pack(pady=10)
    clear_button = tk.Button(menu_page, text='Clear All Data', height=2, width=40, command=lambda: [clear(), clear_page.tkraise()])
    clear_button.pack(pady=10)

    root.mainloop()
    '''
    input_teams()
    input_matches()
    display_rankings()
    display_team()
    edit_match()
    edit_team()
    display_rankings()
    clear()
    display_team()
    display_rankings()
    '''

    
if __name__ == '__main__':
    main()