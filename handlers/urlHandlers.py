from urllib.parse import urlparse, parse_qs

def analyze_url_meta(url):
    parsed_url = urlparse(url)

    response = f"It has {parsed_url.scheme} protocol,\n"
    response += f"Domain is '{parsed_url.netloc}'\n"

    path_steps = parsed_url.path.strip('/').split('/')
    response += f"The path to the resource has {len(path_steps)} step(s) - {', '.join(path_steps)}\n"

    query_params = parse_qs(parsed_url.query)
    if query_params:
        response += f"Query parameters ({len(query_params)}) are present: {query_params}\n"
    else:
        response += "No query parameters\n"

    return response
