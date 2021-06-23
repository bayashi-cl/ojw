use structopt::StructOpt;

#[derive(Debug, StructOpt)]
pub struct New {
    pub contest_id: String,
}
#[derive(Debug, StructOpt)]
pub struct Test {
    pub problem_id: String,
}
#[derive(Debug, StructOpt)]
pub struct Submit {
    pub problem_id: String,
}

#[derive(Debug, StructOpt)]
pub enum Command {
    #[structopt(name = "new")]
    New(New),
    #[structopt(name = "test")]
    Test(Test),
    #[structopt(name = "submit")]
    Submit(Submit),
}

#[derive(Debug, StructOpt)]
#[structopt(name = "classify")]
pub struct Args {
    #[structopt(subcommand)]
    pub command: Command,
}

fn main() {
    let opt = Args::from_args();
    println!("{:?}", opt);
}
