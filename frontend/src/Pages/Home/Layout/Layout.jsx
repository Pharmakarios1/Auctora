import Spotlight from "../Spotlight";
import Separator from "../../../Components/Separator";
import AuctionListing from "../AuctionListing";
import Category from "../Category";

const Layout = () => {
  return (
    <div>
      <Spotlight />
      <Separator title={`ONGOING AUCTIONS`} />
      <AuctionListing />
      <Category />
    </div>
  );
};

export default Layout;
