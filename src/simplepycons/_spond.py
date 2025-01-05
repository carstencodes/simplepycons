#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class SpondIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spond"

    @property
    def original_file_name(self) -> "str":
        return "spond.svg"

    @property
    def title(self) -> "str":
        return "Spond"

    @property
    def primary_color(self) -> "str":
        return "#EE4353"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spond</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm-1.403 2.281a3.767 3.767 0 00-.17 2.847c.61 1.79
 2.336 2.772 4.069 3.213 2.633.672 4.715 1.388 5.892 2.502 1.037.982
 1.435 2.416.803 4.618-.17.59-.486 1.124-.802
 1.643-.125-.706-.424-1.411-.924-2.094-3.269-4.462-10.438-3.57-13.174-7.307-.803-1.096-.747-2.236.092-3.288.979-1.226
 2.69-1.917 4.214-2.134zm3.163.11c.138-.01.281.002.43.036a9.835 9.835
 0 017.076
 6.318c-1.514-1.132-3.655-1.86-6.233-2.517-1.528-.39-2.3-1.087-2.542-1.798-.326-.956.308-1.98
 1.27-2.04zM3.611 6.895c.125.706.424 1.412.924 2.094 3.269 4.462
 10.438 3.57 13.174 7.307.803 1.095.747 2.236-.092 3.288-.979
 1.226-2.69 1.916-4.214
 2.133.427-.89.489-1.91.17-2.846-.61-1.79-2.336-2.772-4.069-3.213-2.633-.672-4.715-1.388-5.892-2.502-1.037-.982-1.435-2.416-.803-4.618.17-.59.486-1.124.802-1.643zm-.877
 8.36c1.514 1.13 3.655 1.858 6.233 2.516 1.528.39 2.3 1.087 2.542
 1.798.336.985-.347 2.042-1.357 2.042-.11 0-.225-.012-.342-.039a9.835
 9.835 0 01-7.076-6.318z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
