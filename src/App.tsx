import React, { useState, useEffect } from 'react';
import { ShoppingBag, Search, Filter, Plus, User, MessageCircle, LogIn, LogOut } from 'lucide-react';

// Mock data for initial visualization
const MOCK_ADS = [
  {
    id: 1,
    title: 'iPhone 13 Pro Max - 256GB',
    price: 75000,
    description: 'В отличном состоянии, полный комплект. Использовался бережно.',
    author: { first_name: 'Александр', last_name: 'И.' },
    created_at: '2023-10-25T10:00:00Z',
    image: 'https://images.unsplash.com/photo-1632661674596-df8be070a5c5?auto=format&fit=crop&q=80&w=400'
  },
  {
    id: 2,
    title: 'Велосипед горный Rockrider',
    price: 25000,
    description: 'Почти новый, катались пару раз. 21 скорость, дисковые тормоза.',
    author: { first_name: 'Мария', last_name: 'П.' },
    created_at: '2023-10-24T15:30:00Z',
    image: 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&q=80&w=400'
  },
  {
    id: 3,
    title: 'PlayStation 5 + 2 геймпада',
    price: 48000,
    description: 'Версия с дисководом. Не шумит, не греется. Игры в подарок.',
    author: { first_name: 'Дмитрий', last_name: 'К.' },
    created_at: '2023-10-23T09:15:00Z',
    image: 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&q=80&w=400'
  }
];

function App() {
  const [ads, setAds] = useState(MOCK_ADS);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      {/* Navigation */}
      <nav className="bg-white shadow-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center gap-2">
              <div className="bg-blue-600 p-2 rounded-lg">
                <ShoppingBag className="text-white w-6 h-6" />
              </div>
              <span className="text-xl font-bold text-gray-900 tracking-tight">Skydash Ads</span>
            </div>

            <div className="hidden md:flex flex-1 max-w-md mx-8">
              <div className="relative w-full">
                <input
                  type="text"
                  placeholder="Поиск объявлений..."
                  className="w-full bg-gray-100 border-none rounded-full py-2 pl-10 pr-4 focus:ring-2 focus:ring-blue-500"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
                <Search className="absolute left-3 top-2.5 text-gray-400 w-5 h-5" />
              </div>
            </div>

            <div className="flex items-center gap-4">
              {isLoggedIn ? (
                <>
                  <button className="flex items-center gap-2 text-gray-700 hover:text-blue-600 font-medium">
                    <Plus className="w-5 h-5" />
                    <span className="hidden sm:inline">Создать</span>
                  </button>
                  <button className="flex items-center gap-2 text-gray-700 hover:text-blue-600 font-medium">
                    <User className="w-5 h-5" />
                    <span className="hidden sm:inline">Профиль</span>
                  </button>
                  <button 
                    onClick={() => setIsLoggedIn(false)}
                    className="p-2 text-gray-500 hover:text-red-500"
                  >
                    <LogOut className="w-5 h-5" />
                  </button>
                </>
              ) : (
                <button 
                  onClick={() => setIsLoggedIn(true)}
                  className="bg-blue-600 text-white px-6 py-2 rounded-full font-semibold hover:bg-blue-700 transition shadow-md flex items-center gap-2"
                >
                  <LogIn className="w-4 h-4" />
                  Войти
                </button>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* Hero / Header */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
              <h1 className="text-3xl font-extrabold text-gray-900">Каталог товаров</h1>
              <p className="mt-2 text-gray-500">Найдено {ads.length} актуальных предложений</p>
            </div>
            <div className="flex gap-2">
              <button className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium hover:bg-gray-50">
                <Filter className="w-4 h-4" />
                Фильтры
              </button>
              <select className="bg-white border border-gray-300 rounded-lg text-sm font-medium py-2 px-4 hover:bg-gray-50">
                <option>Сначала новые</option>
                <option>Дешевле</option>
                <option>Дороже</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          {ads.map((ad) => (
            <div key={ad.id} className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 group">
              <div className="relative aspect-video overflow-hidden">
                <img 
                  src={ad.image} 
                  alt={ad.title}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                />
                <div className="absolute top-3 right-3 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-sm font-bold text-gray-900 shadow-sm">
                  {ad.price.toLocaleString()} ₽
                </div>
              </div>
              <div className="p-5">
                <h3 className="font-bold text-lg text-gray-900 line-clamp-1 group-hover:text-blue-600 transition-colors">
                  {ad.title}
                </h3>
                <p className="text-gray-500 text-sm mt-2 line-clamp-2 h-10">
                  {ad.description}
                </p>
                <div className="mt-6 flex items-center justify-between border-t border-gray-100 pt-4">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold text-xs">
                      {ad.author.first_name[0]}
                    </div>
                    <span className="text-sm font-medium text-gray-700">{ad.author.first_name}</span>
                  </div>
                  <div className="flex items-center gap-1 text-gray-400 text-xs">
                    <MessageCircle className="w-4 h-4" />
                    <span>Отзывы</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-20">
        <div className="max-w-7xl mx-auto px-4 py-12 text-center">
          <p className="text-gray-400 text-sm">© 2023 Skydash Board. Дипломный проект SB1.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
