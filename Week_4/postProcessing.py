def post_process(predictions):
    label_mapping = {
        0: 'Cat',
        1: 'Dog',
        2: 'Bird'
    }

    translated_predictions = [label_mapping[label] for label in predictions]
    return translated_predictions

# Example usage:
predictions = [0, 1, 2, 1, 0]
translated_predictions = post_process(predictions)

print(translated_predictions)