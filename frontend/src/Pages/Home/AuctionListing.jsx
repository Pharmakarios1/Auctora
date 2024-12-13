import { productListArr } from "../../Constants";
import Card from "../../Components/Card";
import { useState } from "react";
import Button from "../../Components/Button";

// const buildArr = {

//     imgUrl: String;
//     itemName: String;
//     sellerName: String;
//     bid:Number;
//     bidTimes:Number;
//     price:Number;
//     countDown:Number;
// }
const AuctionListing = () => {
  const [visibleCards, setVisibleCards] = useState(4); // Show 4 cards initially

  const isDesktop = window.innerWidth >= 768; // Example breakpoint

  const loadMore = () => {
    setVisibleCards((prev) => Math.min(prev + 4, productListArr.length));
  };

  const displayedCards = isDesktop
    ? productListArr
    : productListArr.slice(0, visibleCards);
  return (
    <div className="mt-10">
      <div className="formatter grid place-items-center grid-cols-2 gap-2 lg:gap-x-4 lg:grid-cols-3 xl:grid-cols-4">
        {displayedCards.map((item, idx) => {
          return (
            <Card
              key={idx}
              imgUrl={item.imgUrl}
              itemName={item.itemName}
              bid={item.bid}
              bidTimes={item.bidTimes}
              sellerName={item.sellerName}
              price={item.price}
              countDown={item.countDown}
            />
          );
        })}
      </div>
      <div className="formatter flex justify-center">
        <div className="w-full mt-5 ">
          <Button
            label={`View All`}
            onClick={loadMore}
            className={`md:w-[200px]`}
          />
        </div>
      </div>
    </div>
  );
};

export default AuctionListing;
