fn main() {
    let vars: Vec<(String, String)> = std::env::vars().collect::<Vec<_>>();
    let map = vars.into_iter().map(|(k,v)| format!("{k}={v}")).collect::<Vec<_>>().join(";");
    println!("{map}");
}
