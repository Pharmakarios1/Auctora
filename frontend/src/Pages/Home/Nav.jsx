import { Link, NavLink } from "react-router-dom";

import Search from "../../Components/Search";
import { likee, logo, search_glass, user } from "../../Constants";
import { useEffect } from "react";
import { useState } from "react";
import { LuAlignJustify } from "react-icons/lu";
import { RiCloseLargeFill } from "react-icons/ri";

const Nav = () => {
  // NavLink Array
  const menuArr = [
    { _id: 1, label: "Home", link: "/" },
    { _id: 2, label: "List", link: "/list" },
    { _id: 3, label: "About Us", link: "/about-us" },
  ];
  // mobile switch state and handler
  const [isMobile, setIsMobile] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const closeMoblieMenu = () => {
    setIsMenuOpen(() => !isMenuOpen);
  };
  useEffect(() => {
    window.addEventListener("resize", () => {
      window.innerWidth <= 768 ? setIsMobile(true) : setIsMobile(false);
    });

    return () => {
      window.removeEventListener("resize", () => {
        window.innerWidth <= 768 ? setIsMobile(true) : setIsMobile(false);
      });
    };
  }, []);

  // Search bar handler
  const handleSearch = () => {
    console.log("searching...");
  };

  return (
    <div className="h-[36px] my-[20px] ">
      {/* MobileMenu */}
      {isMobile ? (
        <div className="formatter flex justify-between items-center">
          <div className="flex items-center gap-4 relative">
            {isMenuOpen ? (
              <RiCloseLargeFill
                size={30}
                onClick={closeMoblieMenu}
                className="cursor-pointer"
              />
            ) : (
              <LuAlignJustify
                size={30}
                onClick={closeMoblieMenu}
                className="cursor-pointer"
              />
            )}
            <Link to={`/`}>
              <img src={logo} alt="logo" className="w-[130px]" />
            </Link>
          </div>
          <nav className="text-[16px] absolute z-10 text-white bg-gradient-to-r from-[#7B2334] to-[#9F3247] left-0 top-0 w-full p-10">
            <ul className="flex flex-col gap-8 pb-10 m-auto">
              {menuArr.map((item) => (
                <NavLink key={item._id} to={item.link}>
                  {item.label}
                </NavLink>
              ))}
            </ul>
            <div className="flex gap-4 mr-auto">
              <Search
                img={search_glass}
                placeholder={`Search for Products`}
                onClick={handleSearch}
              />
              <RiCloseLargeFill
                size={40}
                className="cursor-pointer"
                onClick={closeMoblieMenu}
              />
            </div>
          </nav>
          <div className="flex gap-4">
            <img src={search_glass} alt="" className="h-4 w-4 cursor-pointer" />
            <img src={likee} alt="" className="h-4 w-4 cursor-pointer" />
            <img src={user} alt="" className="h-4 w-4 cursor-pointer" />
          </div>
        </div>
      ) : (
        // DesktopMenu
        <div className="formatter flex justify-between items-center">
          <Link to={`/`}>
            <img src={logo} alt="logo" className="w-[130px]" />
          </Link>
          <nav className="sm:text-[15px] text-[16px] ">
            <ul className="flex gap-8">
              {menuArr.map((item) => (
                <NavLink key={item._id} to={item.link}>
                  {item.label}
                </NavLink>
              ))}
            </ul>
          </nav>
          <Search
            className={`sm:w-[250px] xl:w-[700px]`}
            img={search_glass}
            onClick={handleSearch}
            placeholder={`Search for products...`}
          />
          <div className="flex gap-4">
            <img src={likee} alt="" className="h-4 w-4 cursor-pointer" />
            <img src={user} alt="" className="h-4 w-4 cursor-pointer" />
          </div>
        </div>
      )}
    </div>
  );
};

export default Nav;
