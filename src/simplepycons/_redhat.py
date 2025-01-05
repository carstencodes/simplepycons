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


class RedHatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redhat"

    @property
    def original_file_name(self) -> "str":
        return "redhat.svg"

    @property
    def title(self) -> "str":
        return "Red Hat"

    @property
    def primary_color(self) -> "str":
        return "#EE0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Red Hat</title>
     <path d="M16.009 13.386c1.577 0 3.86-.326 3.86-2.202a1.765 1.765
 0 0
 0-.04-.431l-.94-4.08c-.216-.898-.406-1.305-1.982-2.093-1.223-.625-3.888-1.658-4.676-1.658-.733
 0-.947.946-1.822.946-.842 0-1.467-.706-2.255-.706-.757
 0-1.25.515-1.63 1.576 0 0-1.06 2.99-1.197 3.424a.81.81 0 0
 0-.028.245c0 1.162 4.577 4.974 10.71 4.974m4.101-1.435c.218 1.032.218
 1.14.218 1.277 0 1.765-1.984 2.745-4.593
 2.745-5.895.004-11.06-3.451-11.06-5.734a2.326 2.326 0 0 1
 .19-.925C2.746 9.415 0 9.794 0 12.217c0 3.969 9.405 8.861 16.851
 8.861 5.71 0 7.149-2.582 7.149-4.62 0-1.605-1.387-3.425-3.887-4.512"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.redhat.com/en/about/brand/new-bra'''

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
