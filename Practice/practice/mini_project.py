data = {
    # Your JSON data here
}

annotations = data["annotations"]

for annotation in annotations:
    result = annotation["result"]
    print("Annotation ID:", annotation["id"])
    
    for item in result:
        value = item["value"]
        labels = value["labels"]
        
        text = value["text"]
        first_5_labels = labels[:5] if len(labels) >= 5 else labels
        
        print("Text:", text)
        print("First 5 Labels:", first_5_labels)
        print("----")
