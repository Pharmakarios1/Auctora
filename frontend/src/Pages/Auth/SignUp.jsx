import AuthForm from "../../Components/auth/AuthForm";
import AuthNote from "../../Components/auth/AuthNote";
import Breadcrumbs from "../../Components/Breadcrumbs";
import Button from "../../Components/Button";

const SignUp = () => {
  const createAccount = () => {
    console.log("creating");
  };
  return (
    <div className="bg-[#F2F0F1] min-h-screen">
      <div className="formatter">
        <div className="py-6">
          <Breadcrumbs />
          <div className="flex w-full">
            <AuthForm />
            <AuthNote
              heading={`Create Account`}
              body={`Create an account to dive into the world of auctions and unveil hidden treasures. As a member of Auctora, you'll gain exclusive access to bid on unique, one-of-a-kind items, from vintage gems to intriguing antiques. Don't miss out on the excitement – sign up now and embark on a journey where every bid is a step closer to uncovering extraordinary finds! Join the auction adventure today!
`}
              button={
                <Button
                  label={`Already have an account? Login here`}
                  onClick={createAccount}
                />
              }
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
