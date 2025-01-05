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


class PersonioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "personio"

    @property
    def original_file_name(self) -> "str":
        return "personio.svg"

    @property
    def title(self) -> "str":
        return "Personio"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Personio</title>
     <path d="M21.603 24H2.47v-1.563h19.133Zm-6.167-4.044c.557.145
 1.137-.244
 1.303-.867.166-.624-.157-1.25-.713-1.39-.556-.142-1.137.24-1.304.865-.167.624.156
 1.25.714 1.39zM22.37.676c-1.737-1.347-5.387-.43-8.145.576A41.707
 41.705 0 0 0 5.64 5.625C3.624 6.985 1.135 8.987.748 10.814a1.43 1.43
 0 0 0 .28 1.263c.505.59 1.354.576 1.516.568a.781.781 0 0 0
 .51-1.368.783.783 0 0 0-.58-.193.877.877 0 0 1-.181-.016c.58-2.136
 6.69-6.232 12.47-8.342 3.858-1.408 5.964-1.342
 6.649-.81.284.22.433.487.23 1.062-.545 1.535-3.2 3.96-7.108
 6.48-.725.467-1.434.898-2.11 1.29.544-1.92 1.1-3.88
 1.582-5.561a.782.782 0 0 0-1.504-.43 2070.72 2070.634 0 0 0-2.002
 7.05c-1.564.811-2.754 1.3-3.22 1.366a.783.783 0 0 0-1.025
 1.095c.134.226.4.476.929.476.088 0 .177-.007.264-.02.54-.073
 1.417-.395 2.485-.884-.758 2.702-1.373 4.975-1.407 5.282a.781.781 0 0
 0 .69.858.668.668 0 0 0 .087 0 .783.783 0 0 0
 .775-.685c.062-.38.822-3.133 1.746-6.42a58.241 58.239 0 0 0
 4.01-2.401c5.435-3.587 7.007-5.917
 7.362-7.241.277-1.02-.017-1.93-.825-2.557z" />
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
