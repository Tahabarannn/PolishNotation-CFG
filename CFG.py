def generate_language(cfg, current, current_word, words):
    if not current:
        words.append(current_word)
        return

    if current in cfg:
        for production in cfg[current]:
            generate_language(cfg, production, current_word, words)
    else:
        for symbol in current:
            generate_language(cfg, '', current_word + symbol, words)

def remove_duplicates(words):
    return list(set(words))

def get_cfg_from_user():
    cfg = {}
    non_terminals = input("Enter non-terminals separated by commas: ").split(',')

    for non_terminal in non_terminals:
        productions = input(f"Enter productions for {non_terminal}: ").split(',')
        cfg[non_terminal] = productions

    return cfg

def main():
    # Get CFG from the user
    user_cfg = get_cfg_from_user()

    # Generate the language
    all_words = []
    generate_language(user_cfg, 'S', '', all_words)

    # Find repeated words
    repeated_words = [word for word in all_words if all_words.count(word) > 1]

    # Display the results
    print("\nGenerated Words:")
    print(', '.join(all_words))
    print("\nRepeated Words:")
    print(', '.join(remove_duplicates(repeated_words)))

if __name__ == "__main__":
    main()
