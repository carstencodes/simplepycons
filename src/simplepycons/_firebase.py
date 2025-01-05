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


class FirebaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "firebase"

    @property
    def original_file_name(self) -> "str":
        return "firebase.svg"

    @property
    def title(self) -> "str":
        return "Firebase"

    @property
    def primary_color(self) -> "str":
        return "#DD2C00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Firebase</title>
     <path d="M19.455
 8.369c-.538-.748-1.778-2.285-3.681-4.569-.826-.991-1.535-1.832-1.884-2.245a146
 146 0 0 0-.488-.576l-.207-.245-.113-.133-.022-.032-.01-.005L12.57
 0l-.609.488c-1.555 1.246-2.828 2.851-3.681 4.64-.523 1.064-.864
 2.105-1.043
 3.176-.047.241-.088.489-.121.738-.209-.017-.421-.028-.632-.033-.018-.001-.035-.002-.059-.003a7.46
 7.46 0 0 0-2.28.274l-.317.089-.163.286c-.765 1.342-1.198 2.869-1.252
 4.416-.07 2.01.477 3.954 1.583 5.625 1.082 1.633 2.61 2.882 4.42
 3.611l.236.095.071.025.003-.001a9.59 9.59 0 0 0
 2.941.568q.171.006.342.006c1.273 0 2.513-.249
 3.69-.742l.008.004.313-.145a9.63 9.63 0 0 0 3.927-3.335c1.01-1.49
 1.577-3.234 1.641-5.042.075-2.161-.643-4.304-2.133-6.371m-7.083
 6.695c.328 1.244.264 2.44-.191
 3.558-1.135-1.12-1.967-2.352-2.475-3.665-.543-1.404-.87-2.74-.974-3.975.48.157.922.366
 1.315.622 1.132.737 1.914 1.902 2.325 3.461zm.207
 6.022c.482.368.99.712 1.513 1.028-.771.21-1.565.302-2.369.273a8 8 0 0
 1-.373-.022c.458-.394.869-.823
 1.228-1.279zm1.347-6.431c-.516-1.957-1.527-3.437-3.002-4.398-.647-.421-1.385-.741-2.194-.95.011-.134.026-.268.043-.4.014-.113.03-.216.046-.313.133-.689.332-1.37.589-2.025.099-.25.206-.499.321-.74l.004-.008c.177-.358.376-.719.61-1.105l.092-.152-.003-.001c.544-.851
 1.197-1.627 1.942-2.311l.288.341c.672.796 1.304 1.548 1.878 2.237
 1.291 1.549 2.966 3.583 3.612 4.48 1.277 1.771 1.893 3.579 1.83
 5.375-.049 1.395-.461 2.755-1.195 3.933-.694 1.116-1.661 2.05-2.8
 2.708-.636-.318-1.559-.839-2.539-1.599.79-1.575.952-3.28.479-5.072zm-2.575
 5.397c-.725.939-1.587 1.55-2.09
 1.856-.081-.029-.163-.06-.243-.093l-.065-.026c-1.49-.616-2.747-1.656-3.635-3.01-.907-1.384-1.356-2.993-1.298-4.653.041-1.19.338-2.327.882-3.379.316-.07.638-.114.96-.131l.084-.002c.162-.003.324-.003.478
 0 .227.011.454.035.677.07.073 1.513.445 3.145 1.105 4.852.637 1.644
 1.694 3.162 3.144 4.515z" />
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
