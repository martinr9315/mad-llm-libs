import clsx from 'clsx';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

export function Button({ children, disabled, ...rest }: ButtonProps) {
    // Modify onClick in rest
    const originalOnClick = rest.onClick;
    rest.onClick = (e) => {
      if (disabled) {
        e.preventDefault();
      } else if (originalOnClick) {
        originalOnClick(e);
      }
    };
  
    return (
      <button
        {...rest}
        disabled={disabled}
        className={clsx(
          'flex p-2 h-10 items-center rounded-lg bg-blue-900 px-4 text-sm font-medium text-white transition-colors hover:bg-blue-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 active:bg-blue-600 aria-disabled:cursor-not-allowed aria-disabled:opacity-50',
          disabled ? 'bg-gray-500 hover:bg-gray-500' : '',
        )}
      >
        {children}
      </button>
    );
  }
