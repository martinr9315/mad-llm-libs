'use client';
import { Button } from './components/button';
import { useState } from 'react';

interface MadLibsData {
  story: string;
  blanks: string;
  status: string;
  message: string;
}

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [madLibsData, setMadLibsData] = useState<MadLibsData | null>(null);
  const [revealStory, setRevealStory] = useState(false);
  const [userInputs, setUserInputs] = useState<string[]>([]);

  const handleClick = async () => {
    setLoading(true);
    setMadLibsData(null);
    setRevealStory(false);
    try {
      const response = await fetch('/api/madlibs');
      const data = await response.json();
      setMadLibsData(data);
      setUserInputs(new Array(data.blanks.split(', ').length).fill(''));
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleRevealStory = () => {
    setRevealStory(true);
  };

  const allInputsFilled = userInputs.every(input => input !== '');

  return (
    <main className="flex min-h-screen flex-col items-center p-2 bg-gray-200 text-blue-900 font-sans">
      <h1 className="text-5xl font-bold p-10">MadLLMLibs</h1>
      {madLibsData && !revealStory &&(
        <div className="p-2 bg-white border-2 border-dashed border-blue-900 rounded-lg">
          <strong className="text-red-600">Fill in the blanks!</strong>
          {madLibsData.blanks.split(', ').map((blank, index) => (
            <div key={index} className="flex items-center p-1">
              <span>{blank}:</span>
              <input 
                type="text" 
                className="ml-2 rounded-lg border-2 border-gray-300 p-2 border-blue-900" 
                value={userInputs[index] || ''} 
                onChange={(e) => {
                  const newInputs = [...userInputs];
                  newInputs[index] = e.target.value;
                  setUserInputs(newInputs);
                }} 
              />
            </div>
          ))}
        </div>
      )}
    
      {madLibsData && revealStory && (
        <div className="p-2 w-1/4 bg-white border-2 border-dashed border-blue-900 rounded-lg">
          <h2 className="p-2">{madLibsData.story.split('_').map((part, index) => (
            <>{part}{userInputs[index]}</>
          ))}</h2>
        </div>
      )}
      <div className='p-3'/>
      {madLibsData && revealStory && (
        <Button onClick={handleClick} disabled={loading}>
           {loading ? 'Loading...' : 'Generate new MadLibs'}
        </Button>
      )}
      {!madLibsData && (
      <Button onClick={handleClick} disabled={loading}>
        {loading ? 'Loading...' : 'Generate MadLibs'}
      </Button>)}
      {madLibsData && !revealStory && (
        <Button onClick={handleRevealStory} disabled={!allInputsFilled}>
          Reveal Story
        </Button>
      )}
    </main>
  );
}

